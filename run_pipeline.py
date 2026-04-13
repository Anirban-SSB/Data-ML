from config.config_loader import load_config
from config.logger import setup_logger

from etl.extract.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

from quality.validator import validate_data
from utils.metrics import Metrics


# =========================
# PATH CLEANER
# =========================
def clean_path(path: str) -> str:
    """
    Cleans malformed file paths like:
    file_path:"C:\\Users\\file.xlsx"
    """
    if not isinstance(path, str):
        return path

    # Remove 'file_path:' if present
    if "file_path:" in path:
        path = path.split("file_path:")[-1]

    # Remove quotes
    path = path.strip().strip('"').strip("'")

    return path


# =========================
# CONFIG NORMALIZER
# =========================
def normalize_source_config(src: dict):
    """
    Converts any config format into a standard dictionary
    """

    source_type = src.get("type")

    if not source_type:
        raise ValueError("Missing 'source.type' in config")

    raw_config = src.get(source_type)

    # Case 1: dict
    if isinstance(raw_config, dict):
        cleaned = {
            k: clean_path(v) for k, v in raw_config.items()
        }
        return source_type, cleaned

    # Case 2: string
    if isinstance(raw_config, str):
        return source_type, {"file_path": clean_path(raw_config)}

    # Case 3: flat structure
    if "file_path" in src:
        return source_type, {"file_path": clean_path(src["file_path"])}

    raise ValueError(f"Invalid config format for source type: {source_type}")


# =========================
# MAIN PIPELINE
# =========================
def run_pipeline():
    config = load_config()
    logger = setup_logger(config)
    metrics = Metrics()

    logger.info("Pipeline started")

    try:
        # =====================
        # NORMALIZE CONFIG
        # =====================
        src = config.get("source", {})
        source_type, source_config = normalize_source_config(src)

        logger.info(f"Using source: {source_type}")
        logger.info(f"Source config: {source_config}")

        # =====================
        # EXTRACT
        # =====================
        df = extract_data({
            "source_type": source_type,
            **source_config
        })

        # =====================
        # VALIDATE
        # =====================
        logger.info(f"Data Quality: {validate_data(df)}")

        # =====================
        # TRANSFORM
        # =====================
        df = transform_data(df, config.get("transform", {}))

        # =====================
        # LOAD
        # =====================
        load_data(df, config.get("load", {}))

        # =====================
        # METRICS
        # =====================
        logger.info(f"Execution Metrics: {metrics.end()}")
        logger.info("Pipeline completed successfully")

    except Exception as e:
        logger.error(f"Pipeline failed: {str(e)}", exc_info=True)
        raise


# =========================
# ENTRY POINT
# =========================
if __name__ == "__main__":
    run_pipeline()