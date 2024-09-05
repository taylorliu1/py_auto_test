import os
import json


class JsonReader:
    def __init__(self, jsonf):
        if os.path.exists(jsonf):
            self.jsonf = jsonf
        else:
            raise FileNotFoundError("File not exists")
        self._data = None

    def data(self):
        if not self._data:
            with open(self.jsonf, "rb") as f:
                contents = f.read()
                self._data = json.loads(contents)
        return self._data
