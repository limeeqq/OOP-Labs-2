from DAL.json_provider import JsonProvider

class StudentService:
    def __init__(self):
        self.repo = JsonProvider()
        self.students = self.repo.load()

    def add(self, s):
        self.students.append(s)
        self.repo.save(self.students)

    def get_summer_3rd(self):
        return [s for s in self.students if s.course == 3 and s.is_summer()]