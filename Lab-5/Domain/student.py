from datetime import datetime

class Student:
    def __init__(self, ln, fn, course, ticket, bday, group):
        self.last_name, self.first_name = ln, fn
        self.course, self.ticket = int(course), ticket
        self.birth_date, self.group = bday, group

    def transfer(self):
        if self.course < 6: self.course += 1

    def is_summer(self):
        try: return datetime.strptime(self.birth_date, "%d-%m-%Y").month in [6, 7, 8]
        except: return False

    def to_dict(self): return self.__dict__
    
    @staticmethod
    def from_dict(d): 
        return Student(d['last_name'], d['first_name'], d['course'], d['ticket'], d['birth_date'], d['group'])
    
    def __str__(self): return f"{self.last_name} {self.first_name}, Курс: {self.course}, Група: {self.group}"