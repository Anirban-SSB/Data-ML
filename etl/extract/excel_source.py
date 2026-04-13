import pandas as pd

def extract_from_excel(config):
    return pd.read_excel(config["file_path"])