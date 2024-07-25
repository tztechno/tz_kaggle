
from sklearn.metrics import roc_auc_score


def total_auc(solution: pd.DataFrame, submission: pd.DataFrame):
    v_gt = abs(np.asarray(solution.values) - 1)
    v_pred = np.array([1.0 - x for x in submission.values])
    auc = roc_auc_score(v_gt, v_pred)
    return auc


def pauc_above_tpr(solution: pd.DataFrame, submission: pd.DataFrame, min_tpr: float=0.80):
    v_gt = abs(np.asarray(solution.values)-1)
    v_pred = np.array([1.0 - x for x in submission.values])
    max_fpr = abs(1-min_tpr)
    partial_auc_scaled = roc_auc_score(v_gt, v_pred, max_fpr=max_fpr)
    partial_auc = 0.5 * max_fpr**2 + (max_fpr - 0.5 * max_fpr**2) / (1.0 - 0.5) * (partial_auc_scaled - 0.5)
    return partial_auc
