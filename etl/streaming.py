import time

def stream_data(df, size=5):
    for i in range(0, len(df), size):
        yield df.iloc[i:i+size]
        time.sleep(1)