import json
import os

class Saver:
    def __init__(self, file):
        self.file = file

    def save(self, data):
        with open(self.file, "w") as file:
            json.dump(data, file, indent=4)

    def read(self):
        if not os.path.exists(self.file) or os.stat(self.file).st_size == 0:
            return []
        with open(self.file, "r") as file:
            return json.load(file)
