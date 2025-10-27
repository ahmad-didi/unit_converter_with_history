import json
import os

class HistoryManager:
    FILE = os.path.join(os.path.dirname(__file__), '..', 'history.json')

    def __init__(self):
        self.FILE = os.path.normpath(self.FILE)
        if not os.path.exists(self.FILE):
            with open(self.FILE, 'w') as f:
                json.dump([], f)

    def load(self):
        with open(self.FILE, 'r') as f:
            return json.load(f)

    def add(self, record):
        h = self.load()
        h.append(record)
        with open(self.FILE, 'w') as f:
            json.dump(h, f, indent=2)

    def clear(self):
        with open(self.FILE, 'w') as f:
            json.dump([], f)
