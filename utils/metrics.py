import time

class Metrics:
    def __init__(self):
        self.start = time.time()

    def end(self):
        return {"execution_time": round(time.time() - self.start, 2)}