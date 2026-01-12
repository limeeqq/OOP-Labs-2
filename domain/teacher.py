from .person import Person

class Teacher(Person):
    def __init__(self, first_name, last_name, subject):
        super().__init__(first_name, last_name)
        self.subject = subject

    def get_info(self):
        return f"Teacher: {self.first_name} {self.last_name}, Subject: {self.subject}"