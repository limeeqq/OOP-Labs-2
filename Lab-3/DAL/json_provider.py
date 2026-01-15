import json
import os
from Domain.student import Student

class JsonProvider:
    def __init__(self, filename="students.json"):
        self.filename = filename

    def save_data(self, students):#серіалізація
        data_list = [s.to_dict() for s in students]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data_list, f, indent=4, ensure_ascii=False)
        
    def load_data(self):#десеріалізація
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r", encoding="utf-8") as f:
            data_list = json.load(f)
            return [Student.from_dict(item) for item in data_list]