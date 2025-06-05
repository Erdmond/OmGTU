import numpy as np

def confusion_matrix(y_true, y_pred, classes=None):
    if classes is None:
        classes = np.unique(y_true)
    n_classes = len(classes)
    cm = np.zeros((n_classes, n_classes), dtype=int)
    
    for true, pred in zip(y_true, y_pred):
        i = np.where(classes == true)[0][0]
        j = np.where(classes == pred)[0][0]
        cm[i][j] += 1
    
    return cm

def accuracy(y_true, y_pred):
    correct = np.sum(np.array(y_true) == np.array(y_pred))
    return correct / len(y_true)

def precision(y_true, y_pred, average='macro'):
    cm = confusion_matrix(y_true, y_pred)
    precisions = []
    for i in range(cm.shape[0]):
        tp = cm[i, i]
        fp = np.sum(cm[:, i]) - tp
        precisions.append(tp / (tp + fp) if (tp + fp) > 0 else 0)
    
    if average == 'macro':
        return np.mean(precisions)
    elif average == 'micro':
        total_tp = np.sum(np.diag(cm))
        total_fp = np.sum(cm) - total_tp
        return total_tp / (total_tp + total_fp)
    else:
        return precisions

def recall(y_true, y_pred, average='macro'):
    cm = confusion_matrix(y_true, y_pred)
    recalls = []
    for i in range(cm.shape[0]):
        tp = cm[i, i]
        fn = np.sum(cm[i, :]) - tp
        recalls.append(tp / (tp + fn) if (tp + fn) > 0 else 0)
    
    if average == 'macro':
        return np.mean(recalls)
    elif average == 'micro':
        total_tp = np.sum(np.diag(cm))
        total_fn = np.sum(cm) - total_tp
        return total_tp / (total_tp + total_fn)
    else:
        return recalls

def f1(y_true, y_pred, average='macro'):
    prec = precision(y_true, y_pred, average=None)
    rec = recall(y_true, y_pred, average=None)
    f1_scores = []
    for p, r in zip(prec, rec):
        f1_scores.append(2 * (p * r) / (p + r) if (p + r) > 0 else 0)
    
    if average == 'macro':
        return np.mean(f1_scores)
    elif average == 'micro':
        total_prec = precision(y_true, y_pred, average='micro')
        total_rec = recall(y_true, y_pred, average='micro')
        return 2 * (total_prec * total_rec) / (total_prec + total_rec)
    else:
        return f1_scores
