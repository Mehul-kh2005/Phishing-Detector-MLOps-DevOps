from networksecurity.entity.artifact_entity import ClassificationMetricArtifact
from networksecurity.exception.exception import NetworkSecurityException
from sklearn.metrics import accuracy_score,f1_score,precision_score,recall_score
import sys

def get_classification_score(y_true, y_pred) -> ClassificationMetricArtifact:
    try:
        acc = accuracy_score(y_true, y_pred)
        f1 = f1_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred)

        classification_metric = ClassificationMetricArtifact(
            accuracy_score=acc,
            f1_score=f1,
            precision_score=precision,
            recall_score=recall
        )
        return classification_metric

    except Exception as e:
        raise NetworkSecurityException(e, sys)