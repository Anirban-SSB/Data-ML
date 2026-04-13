from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    num = df.select_dtypes(include='number')
    model = IsolationForest()
    df["anomaly"] = model.fit_predict(num)
    return df