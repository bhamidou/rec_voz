import json

class ReadFile:
    file = ""
    def __init__(self, file):
        self.file = file

    def getArr(self):
        arr = []
        with open(self.file, 'r', encoding="utf-8") as f:
            for line in f:
                arr.append(line.strip())
        return arr

    def parseJSON(self):
        with open(self.file, 'r', encoding="utf-8") as f:
            data = json.load(f)
        return data

