from Domain.student import Student
from BLL.service import StudentService

class Menu:
    def __init__(self): self.srv = StudentService()

    def run(self):
        while True:
            c = input("\n1. Add\n2. Find (3rd course, Summer)\n3. Exit\n>> ")
            if c == '1':
                args = [input(x) for x in ["Прізвище: ", "Ім'я: ", "Курс: ", "Квиток: ", "Дата (DD-MM-YYYY): ", "Група: "]]
                self.srv.add(Student(*args))
            elif c == '2':
                [print(s) for s in self.srv.get_summer_3rd()]
            elif c == '3': break