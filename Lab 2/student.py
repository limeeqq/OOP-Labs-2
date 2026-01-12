from datetime import datetime
from person import Person 

class Student(Person):
    def __init__(self, first_name, last_name, course, ticket, birth_year, group_num):
        super().__init__(first_name, last_name)
        self.course = int(course)
        self.ticket = ticket
        self.birth_year = int(birth_year)
        self.group_num = group_num

    def get_info(self):
        return f"{self.last_name} {self.first_name} (Група: {self.group_num})"

    def get_age(self):
        current_year = datetime.now().year
        return current_year - self.birth_year

    def transfer_to_next_course(self):
        self.course += 1

    def __lt__(self, other):
        return self.last_name < other.last_name

    def __gt__(self, other):
        return self.last_name > other.last_name
    
    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.group_num})"