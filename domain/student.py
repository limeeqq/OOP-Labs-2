from .person import Person

class Student(Person):
    def __init__(self, first_name, last_name, course, ticket, birth_date):
        super().__init__(first_name, last_name)
        self.course = int(course)
        self.ticket = ticket
        self.birth_date = birth_date

    def get_info(self):
        return f"Student: {self.first_name} {self.last_name}, Course: {self.course}, Ticket: {self.ticket}, Born: {self.birth_date}"

    # додатковий спів
    def sing(self):
        return "студент співає"