from .csv_source import extract_from_csv
from .api_source import extract_from_api
from .db_source import extract_from_db
from .excel_source import extract_from_excel

import logging

logger = logging.getLogger(__name__)


# =========================
# SOURCE MAPPING (SCALABLE)
# =========================
SOURCE_MAP = {
    "csv": extract_from_csv,
    "api": extract_from_api,
    "db": extract_from_db,
    "excel": extract_from_excel,
}


# =========================
# MAIN FUNCTION
# =========================
def extract_data(config: dict):
    """
    Extract data based on source type
    """

    # 🔍 Validate config
    if not isinstance(config, dict):
        raise ValueError("Config must be a dictionary")

    source_type = config.get("source_type")

    if not source_type:
        raise ValueError("Missing 'source_type' in config")

    # 🔍 Get extractor
    extractor = SOURCE_MAP.get(source_type)

    if not extractor:
        raise ValueError(f"Unsupported source type: {source_type}")

    logger.info(f"Starting extraction from: {source_type}")

    try:
        df = extractor(config)

        if df is None:
            raise ValueError("Extractor returned None")

        if df.empty:
            logger.warning("Extracted dataset is empty")

        logger.info(f"Extraction completed: {len(df)} records")

        return df

    except Exception as e:
        logger.error(f"Extraction failed ({source_type}): {str(e)}", exc_info=True)
        raise