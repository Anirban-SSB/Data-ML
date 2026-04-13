import logging
from models.anomaly_model import detect_anomalies
from analytics.kpi import compute_kpis

logger = logging.getLogger(__name__)

def transform_data(df, config):
    if config.get("drop_nulls"):
        df = df.dropna()

    df = df.fillna(config.get("fillna_value", 0))

    if "sales" in df.columns and "quantity" in df.columns:
        df["price"] = df["sales"] / df["quantity"]

    logger.info(f"KPI: {compute_kpis(df)}")

    if config.get("enable_anomaly_detection"):
        df = detect_anomalies(df)

    return df