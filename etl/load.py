import os

def load_data(df, config):
    path = config["csv"]["output_path"]
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)