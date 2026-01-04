from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest

def behavior_clustering(features):
    """
    Clusters users based on behavioral patterns.
    """
    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(features)
    return clusters

def detect_anomalies(features):
    """
    Detects anomalous behavior using Isolation Forest.
    """
    model = IsolationForest(contamination=0.15, random_state=42)
    anomaly_flag = model.fit_predict(features)
    anomaly_score = model.decision_function(features)
    return anomaly_flag, anomaly_score
