from DAL.json_provider import JsonProvider

class StudentService:
    def __init__(self):
        self.provider = JsonProvider()
        self.students = self.provider.load_data()

    def add(self, student):
        self.students.append(student)
        self.provider.save_data(self.students)

    def get_all(self):
        return self.students

    def get_summer_students_3rd_course(self):
        result = []
        for s in self.students:
            if s.course == 3 and s.is_born_in_summer():
                result.append(s)
        return result