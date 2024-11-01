from read import get_df_results, get_df_segments_with_gt, get_df_annotations
from sklearn import metrics
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

result_path_base = "results/OPP-115/"
OVERWRITE = False   
np.set_printoptions(threshold=np.inf)

RELEVANT_COLUMNS = [  # "Other",
    "User Choice/Control",
    "First Party Collection/Use",
    "Third Party Sharing/Collection",
    "Do Not Track",
    "User Access, Edit and Deletion",
    "Data Security",
    "Data Retention",
    "International and Specific Audiences",
    "Policy Change",
]
RELEVANT_COLUMNS_SHORT = [  # "Other",
    "User Choice...",
    "First Party...",
    "Third Party...",
    "Do Not Track...",
    "User Access...",
    "Data Security",
    "Data Retention",
    "International...",
    "Policy Change",
]

def get_confidence_intervals(df_segments_with_gt, df_results, report):
    if len(df_segments_with_gt["policy_ID"].unique()) == 115:
        # subsample for confidence intervals
        print("Subsample for confidence intervals...")
        sampled_reports = {
            "weighted": [],
            "micro": [],
            "macro": [],
            "samples": [],
            "precision": [],
            "recall": [],
            "f1": [],
        }
        for i in tqdm(range(1000)):
            # get 41 random policies
            sampled_policies = np.random.choice(
                df_segments_with_gt["policy_ID"].unique(), 41, replace=False
            )
            #print(sampled_policies)
            df_sampled_index = df_segments_with_gt.index[
                df_segments_with_gt["policy_ID"].isin(sampled_policies)
            ]
            #print(df_sampled_index)
            y_true_sampled = df_segments_with_gt.loc[df_sampled_index][
                RELEVANT_COLUMNS
            ].values
            y_pred_sampled = df_results.loc[df_sampled_index][RELEVANT_COLUMNS].values
            #print(y_pred_sampled)
            #print(len(y_pred_sampled), len(y_pred_sampled[0]))
            # obtain performance metrics for each class for each subsample
            report_per_class = metrics.precision_recall_fscore_support(
                y_true_sampled, y_pred_sampled, average=None, zero_division=0.0
            )
            sampled_reports["precision"].append(report_per_class[0])
            sampled_reports["recall"].append(report_per_class[1])
            sampled_reports["f1"].append(report_per_class[2])
            # obtain class average performance metrics for each subsample
            for average in ["weighted", "micro", "macro", "samples"]:
                sampled_reports[average].append(
                    metrics.precision_recall_fscore_support(
                        y_true_sampled,
                        y_pred_sampled,
                        average=average,
                        zero_division=0.0,
                    )
                )
    
        # enter subsample intervals into report
        report[
            [
                "lb_conf_precision",
                "lb_conf_recall",
                "lb_conf_f1",
                "ub_conf_precision",
                "ub_conf_recall",
                "ub_conf_f1",
            ]
        ] = 0.0
        for average in ["weighted", "micro", "macro", "samples"]:
            lower_bounds = np.percentile(
                np.asarray(sampled_reports[average])[:, 0:3], 2.5, axis=0
            )
            upper_bounds = np.percentile(
                np.asarray(sampled_reports[average])[:, 0:3], 97.5, axis=0
            )
            report.loc[
                average + " avg", ["lb_conf_precision", "lb_conf_recall", "lb_conf_f1"]
            ] = lower_bounds
            report.loc[
                average + " avg", ["ub_conf_precision", "ub_conf_recall", "ub_conf_f1"]
            ] = upper_bounds
        for metric in ["precision", "recall", "f1"]:
            lower_bounds = np.percentile(
                np.asarray(sampled_reports[metric]), 2.5, axis=0
            )
            upper_bounds = np.percentile(
                np.asarray(sampled_reports[metric]), 97.5, axis=0
            )
            report.loc[RELEVANT_COLUMNS, ["lb_conf_" + metric]] = lower_bounds
            report.loc[RELEVANT_COLUMNS, ["ub_conf_" + metric]] = upper_bounds
    
    return report

if __name__ == "__main__":
    result_paths = []
    for path, subdirs, files in os.walk(result_path_base):
        for name in files:
            if name == "results.xlsx":
                result_paths.append(os.path.join(path, name))

    df_annotations = get_df_annotations("OPP-115")
    for result_path in result_paths:
        if not (OVERWRITE or not os.path.exists(os.path.join(os.path.dirname(result_path), "report.xlsx"))):
            continue
        # obtain data
        print("Obtaining saved data for analysis...")
        df_segments_with_gt = get_df_segments_with_gt("OPP-115", df_annotations, remove_html_tags=True)
        df_segments_with_gt.set_index("complete_segment_ID", inplace=True)
        df_results = get_df_results(result_path)
        df_results.set_index("complete_segment_ID", inplace=True)
        df_segments_with_gt = df_segments_with_gt.loc[df_results.index]
        
        for column in RELEVANT_COLUMNS:
            if column not in df_results.columns:
                df_results[column] = 0

        # obtain dummy arrays, removing other category
        y_true = df_segments_with_gt[RELEVANT_COLUMNS].values
        y_pred = df_results[RELEVANT_COLUMNS].values
        #print(y_pred)
        ind_only_other = np.sum(y_true, axis=1) == 0
        y_true = y_true[~ind_only_other]
        y_pred = y_pred[~ind_only_other]
        #print(y_pred)
        df_results = df_results[~ind_only_other]
        df_segments_with_gt = df_segments_with_gt[~ind_only_other]

        # generate report of performance metrics in df form
        report = metrics.classification_report(
            y_true,
            y_pred,
            target_names=RELEVANT_COLUMNS,
            output_dict=True,
            zero_division=0.0,
        )
        report = pd.DataFrame(report).transpose()
        report  = get_confidence_intervals(df_segments_with_gt, df_results, report)
        # create an overview over the misclassified samples
        print("Create an overview over the misclassified samples...")
        correctly_classified = np.all(np.equal(y_pred, y_true), axis=1)
        ground_truth = y_true[~correctly_classified]
        ground_truth_list = []
        for idx in range(len(ground_truth)):
            ground_truth_list.append(
                list(np.asarray(RELEVANT_COLUMNS)[ground_truth[idx] == 1])
            )
        ground_truth_list = ["&".join(item) for item in ground_truth_list]
        pred = y_pred[~correctly_classified]
        pred_list = []
        for idx in range(len(pred)):
            pred_list.append(list(np.asarray(RELEVANT_COLUMNS)[pred[idx] == 1]))
        pred_list = ["&".join(item) for item in pred_list]
        df_misclassified = df_results[~correctly_classified]
        df_misclassified.loc[:, ["gt"]] = ground_truth_list
        df_misclassified.loc[:, ["pred"]] = pred_list
        df_misclassified = df_misclassified.drop(RELEVANT_COLUMNS, axis=1)
        df_misclassified = df_misclassified.drop("Other", axis=1, errors="ignore")

        # obtaining confusion matrix removing multilabel samples
        print("Obtain confusion matrix...")
        ind_multilabel_true = np.sum(y_true, axis=1) == 1
        y_true = y_true[ind_multilabel_true]
        y_pred = y_pred[ind_multilabel_true]
        ind_multilabel_pred = np.sum(y_pred, axis=1) == 1
        y_true = y_true[ind_multilabel_pred]
        y_pred = y_pred[ind_multilabel_pred]
        disp = metrics.ConfusionMatrixDisplay.from_predictions(
            y_true.argmax(axis=1),
            y_pred.argmax(axis=1),
            display_labels=RELEVANT_COLUMNS_SHORT,
            # normalize="true",
        ).plot(
            xticks_rotation="vertical"
        )  # ,values_format=".2f")
        plt.tight_layout()
        plt.show()

        # saving output
        print("Saving ouput...")
        df_misclassified.to_excel(
            os.path.join(os.path.dirname(result_path), "misclassified.xlsx")
        )
        report.to_excel(os.path.join(os.path.dirname(result_path), "report.xlsx"))
        plt.savefig(os.path.join(os.path.dirname(result_path), "confusion.png"))
        print("Done!")
        # print report with all data
        print("RESULTS OBTAINED FOR ALL DATA:")
        print(report)
