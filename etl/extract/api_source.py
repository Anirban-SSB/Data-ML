import requests
import pandas as pd

def extract_from_api(config):
    res = requests.get(config["url"])
    data = res.json()
    return pd.DataFrame(data)