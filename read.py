"""NOTES:

We created gold
standard data for this problem using a simplified
consolidation approach: if two or more annotators
agreed that a category is present in a segment, then
we labeled that segment with the category

"""

import os
from glob import glob

import pandas as pd
import numpy as np
import json
from tqdm import tqdm
import re

PATH_TO_DATA = "data"

CATEGORY_NAMES = [
    "First Party Collection/Use",
    "Third Party Sharing/Collection",
    "User Choice/Control",
    "User Access, Edit and Deletion",
    "Data Retention",
    "Data Security",
    "Policy Change",
    "Do Not Track",
    "International and Specific Audiences",
    # "Other",
]


def do_remove_html_tags(text):
    clean = re.compile("<.*?>")
    return re.sub(clean, "", text)


def get_df_annotations(dataset_name):
    # read all annotation files into single df
    header_names = [
        "annotation_ID",
        "batch_ID",
        "annotator_ID",
        "policy_ID_other",
        "segment_ID",
        "category_name",
        "attribute_value_pairs",
        "date",
        "policy_URL",
    ]
    df_annotations = []
    for path, subdir, files in os.walk(
        os.path.join(PATH_TO_DATA, dataset_name, "annotations")
    ):
        for file_path in glob(os.path.join(path, "*.csv")):
            annotation = pd.read_csv(file_path, header=None, names=header_names)
            #print(file_path)
            annotation["policy_ID"] = os.path.basename(file_path).split("_")[0]
            df_annotations.append(annotation)
    df_annotations = pd.concat(df_annotations, axis=0, ignore_index=True)
    df_annotations["complete_segment_ID"] = (
        df_annotations["policy_ID"].astype(str)
        + "_"
        + df_annotations["segment_ID"].astype(str)
    )

    # make sure data agrees with paper
    assert len(df_annotations["annotator_ID"].unique()) == 10
    assert len(df_annotations["policy_ID"].unique()) == 115
    assert all(df_annotations.groupby("policy_ID")["annotator_ID"].nunique() == 3)
    assert len(df_annotations) == 23194
    #print(df_annotations)
    return df_annotations


def get_df_segments(dataset_name, n_policies=None, remove_html_tags=False):
    # read all sanatized html files and obtain df with policy_ID, segment_ID and the sentences
    list_of_df_dicts = []
    for path, subdir, files in os.walk(
        os.path.join(PATH_TO_DATA, dataset_name, "sanitized_policies")
    ):
        for ind, file_path in enumerate(glob(os.path.join(path, "*.html"))):
            if n_policies is not None and ind == n_policies:
                break
            policy_ID = os.path.basename(file_path).split("_")[0]
            file_contents = open(file_path, "r")
            segments = file_contents.read().split("|||")
            for ind, segment in enumerate(segments):
                if remove_html_tags:
                    segment = do_remove_html_tags(segment)
                list_of_df_dicts.append(
                    {
                        "policy_ID": int(policy_ID),
                        "segment_ID": ind,
                        "segment_text": segment,
                    }
                )
    df_segments = pd.DataFrame.from_dict(list_of_df_dicts)
    df_segments["complete_segment_ID"] = (
        df_segments["policy_ID"].astype(str)
        + "_"
        + df_segments["segment_ID"].astype(str)
    )
    return df_segments


def get_df_segments_with_gt(dataset_name, df_annotations, remove_html_tags=False):
    # obtain df_segments with groundtruth
    print("Get dataframe with segments text and ground truth...")
    df_segments = get_df_segments(dataset_name, remove_html_tags=remove_html_tags)
    print(df_segments)
    tqdm.pandas()
    df_segments["gt"] = df_segments["complete_segment_ID"].progress_apply(
        get_ground_truth, args=(df_annotations,)
    )
    df_segments = df_segments.join(df_segments["gt"].str.join("|").str.get_dummies())
    #print(df_segments)
    return df_segments


def get_df_segments_for_all_annotators(
    dataset_name, df_annotations, remove_html_tags=False
):
    # obtain df_segments with groundtruth
    print("Get list of dataframes for each annotator with segments and ground truth...")
    df_segments = get_df_segments(dataset_name, remove_html_tags=remove_html_tags)
    tqdm.pandas()
    annotator_ids = df_annotations["annotator_ID"].unique()
    list_df_segments_annotators = []
    for annotator_id in tqdm(annotator_ids):
        df_annotations_for_single_annotator = df_annotations.loc[
            df_annotations["annotator_ID"] == annotator_id
        ]
        df_segments_for_single_annotator = df_segments.loc[
            df_segments["complete_segment_ID"].isin(
                df_annotations_for_single_annotator["complete_segment_ID"]
            )
        ]
        df_segments_for_single_annotator["gt"] = df_segments[
            "complete_segment_ID"
        ].progress_apply(
            get_ground_truth, args=(df_annotations_for_single_annotator, 1)
        )
        df_segments_for_single_annotator = df_segments_for_single_annotator.join(
            df_segments_for_single_annotator["gt"].str.join("|").str.get_dummies()
        )
        list_df_segments_annotators.append(df_segments_for_single_annotator)

    return list_df_segments_annotators


def get_df_results(file_path, return_dummies = True):
    # obtain df_segments with pred
    print("Get dataframe with results...")
    df_results = pd.read_excel(file_path)
    #print(df_results)
    tqdm.pandas()
    df_results["pred"] = df_results["llm_response"].progress_apply(detect_categories)
    #print(df_results)
    if return_dummies:
        df_results = df_results.join(df_results["pred"].str.join("|").str.get_dummies())
    #print(df_results)
    return df_results


def detect_categories(llm_response_value):
    pred = []
    roman_options = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix"]
    alpha_options = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]        
    if not isinstance(llm_response_value, str):
        return pred
    if llm_response_value.isspace():
        return pred
    # if len(llm_response_value) == 1:
        
    if llm_response_value.isdigit():
        llm_response_value = CATEGORY_NAMES[int(llm_response_value) - 1]
    elif llm_response_value.lower() in alpha_options:
            llm_response_value = CATEGORY_NAMES[
                alpha_options.index(llm_response_value.lower())
            ]
    elif llm_response_value.lower() in roman_options:
            llm_response_value = CATEGORY_NAMES[
                roman_options.index(llm_response_value.lower())
            ]

    for category in CATEGORY_NAMES:
        if category == "International and Specific Audiences":
            cats_to_check = ["International", "Specific", "child"]
        elif category == "User Access, Edit and Deletion":
            cats_to_check = ["Access"]
        elif category == "User Choice/Control":
            cats_to_check = ["Choice"]
        elif category == "First Party Collection/Use":
            cats_to_check = ["st Party", "First-Party"]
        elif category == "Third Party Sharing/Collection":
            cats_to_check = ["rd Party", "Third-Party"]
        elif category == "Data Retention":
            cats_to_check = ["retention"]
        elif category == "Data Security":
            cats_to_check = ["security"]
        else:
            cats_to_check = [category]
        for cat_to_check in cats_to_check:
            if cat_to_check.lower() in llm_response_value.lower():
                pred.append(category)
                break
    #if len(pred) > 1:
        #print(pred)
        #print(llm_response_value)
        #print('--------------------------------------------------------------------------------')
    return pred


def get_ground_truth(complete_segment_ID_value, df_annotations, min_occurence=2, column_name="category_name"):
    annotations = df_annotations.loc[
        df_annotations["complete_segment_ID"] == complete_segment_ID_value
    ]
    annotations = annotations[["annotator_ID", column_name]].drop_duplicates()
    annotations = annotations[column_name].value_counts()[
        annotations[column_name].value_counts() >= min_occurence
    ]
    #print(annotations.to_list())
    #print('------------------')
    return annotations.index.to_list()


if __name__ == "__main__":
    # obtain dfs
    df_annotations = get_df_annotations("OPP-115")
    list_df_segments = get_df_segments_for_all_annotators(
        "OPP-115", df_annotations, remove_html_tags=True
    )
    df_segments = get_df_segments("OPP-115", remove_html_tags=True)

    df_segments_with_gt = get_df_segments_with_gt("OPP-115", df_annotations)
    df_results = get_df_results("results/OPP-115/gpt-4/Va/complete/20240422_103113/results.xlsx")
    # merge dfs to obtain one df with both tags and sentences
    df = df_annotations.merge(df_segments, how="left", on="complete_segment_ID")

    # interpret results

    print(df)
