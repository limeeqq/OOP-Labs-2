import json, os
from Domain.student import Student

class JsonProvider:
    def __init__(self, file="data.json"): self.file = file

    def save(self, data):
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump([s.to_dict() for s in data], f, ensure_ascii=False, indent=2)

    def load(self):
        if not os.path.exists(self.file): return []
        with open(self.file, "r", encoding="utf-8") as f:
            return [Student.from_dict(x) for x in json.load(f)]