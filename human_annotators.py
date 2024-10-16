import numpy as np
from tqdm import tqdm
from sklearn import metrics
from analysis import RELEVANT_COLUMNS
from read import (
    get_df_annotations,
    get_df_segments_with_gt,
    get_df_segments_for_all_annotators,
)

if __name__ == "__main__":
    # obtain dfs
    print("Obtaining data from database...")
    df_annotations = get_df_annotations("OPP-115")
    df_segments_with_gt = get_df_segments_with_gt("OPP-115", df_annotations)
    df_segments_with_gt.set_index("complete_segment_ID", inplace=True)
    list_df_segments = get_df_segments_for_all_annotators(
        "OPP-115", df_annotations, remove_html_tags=True
    )
    print("Generate report for each annotator...")
    f1s = []
    for df_results in tqdm(list_df_segments):
        df_results.set_index("complete_segment_ID", inplace=True)
        df_segments_with_gt_copy = df_segments_with_gt.loc[df_results.index]
        for column in RELEVANT_COLUMNS:
            if column not in df_results.columns:
                df_results[column] = 0

        # obtain dummy arrays, removing other category
        y_true = df_segments_with_gt_copy[RELEVANT_COLUMNS].values
        y_pred = df_results[RELEVANT_COLUMNS].values
        ind_only_other = np.sum(y_true, axis=1) == 0
        y_true = y_true[~ind_only_other]
        y_pred = y_pred[~ind_only_other]
        df_results = df_results[~ind_only_other]
        df_segments_with_gt_copy = df_segments_with_gt_copy[~ind_only_other]

        # generate report of performance metrics in df form
        report = metrics.classification_report(
            y_true,
            y_pred,
            target_names=RELEVANT_COLUMNS,
            output_dict=True,
            zero_division=0.0,
        )
        f1s.append(report["micro avg"]["f1-score"])
        print(report)
    print(f1s)
    f1s = np.asarray(f1s)
    print(np.mean(f1s))
print(np.mean(f1s))
print(np.percentile(f1s, 2.5, axis=0))
print(np.percentile(f1s, 97.5, axis=0))
