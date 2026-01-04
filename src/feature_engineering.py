from sklearn.preprocessing import StandardScaler

def scale_features(df):
    """
    Scales numerical user behavior features for machine learning models.
    """
    features = df.drop("user_id", axis=1)
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    return scaled_features
