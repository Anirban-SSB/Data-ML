import sqlite3
import pandas as pd

def extract_from_db(config):
    conn = sqlite3.connect(config["db_path"])
    df = pd.read_sql(config["query"], conn)
    conn.close()
    return df