from .csv_source import extract_from_csv
from .api_source import extract_from_api
from .db_source import extract_from_db
from .excel_source import extract_from_excel

def extract_data(config):
    t = config["source_type"]

    if t == "csv":
        return extract_from_csv(config)
    elif t == "api":
        return extract_from_api(config)
    elif t == "db":
        return extract_from_db(config)
    elif t == "excel":
        return extract_from_excel(config)
    else:
        raise ValueError("Invalid source type")