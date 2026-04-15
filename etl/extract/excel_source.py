import pandas as pd
import os
import logging

logger = logging.getLogger(__name__)


def clean_path(path: str) -> str:
    """
    Cleans malformed file paths like:
    file_path:"C:\\Users\\file.xlsx"
    """
    if not isinstance(path, str):
        return path

    if "file_path:" in path:
        path = path.split("file_path:")[-1]

    return path.strip().strip('"').strip("'")


def extract_from_excel(config: dict):
    """
    Extract data from Excel file

    Expected config:
    {
        "file_path": "path/to/file.xlsx",
        "sheet_name": "Sheet1",        # optional
        "usecols": ["col1", "col2"],   # optional
    }
    """

    # =========================
    # VALIDATION
    # =========================
    if not isinstance(config, dict):
        raise ValueError("Excel config must be a dictionary")

    file_path = config.get("file_path")

    if not file_path:
        raise ValueError("Missing 'file_path' in Excel config")

    file_path = clean_path(file_path)

    # =========================
    # FILE CHECK
    # =========================
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Excel file not found: {file_path}")

    # =========================
    # OPTIONAL PARAMS
    # =========================
    sheet_name = config.get("sheet_name", 0)  # default first sheet
    usecols = config.get("usecols", None)

    logger.info(f"Reading Excel file: {file_path}")
    logger.info(f"Sheet: {sheet_name}")

    # =========================
    # READ EXCEL
    # =========================
    try:
        df = pd.read_excel(
            file_path,
            sheet_name=sheet_name,
            usecols=usecols,
            engine="openpyxl"
        )

        logger.info(f"Excel loaded successfully: {df.shape[0]} rows, {df.shape[1]} columns")

        return df

    except Exception as e:
        logger.error(f"Failed to read Excel file: {str(e)}", exc_info=True)
        raise