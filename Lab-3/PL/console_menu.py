from Domain.student import Student
from BLL.student_service import StudentService

class ConsoleMenu:
    def __init__(self):
        self.service = StudentService()

    def run(self):
        while True:
            print("\nменю")
            print("1. Додати студента")
            print("2. Показати всіх")
            print("3. Знайти (3 курс, літо)")
            print("4. Вихід")
            
            choice = input("Оберіть дію: ")

            if choice == "1":
                ln = input("Прізвище: ")
                fn = input("Ім'я: ")
                cr = input("Курс (число): ")
                tk = input("Квиток: ")
                db = input("Дата нар. (DD-MM-YYYY): ")
                gr = input("Група: ")
                self.service.add(Student(ln, fn, cr, tk, db, gr))
                print("збережено.")

            elif choice == "2":
                for s in self.service.get_all():
                    print(s.get_info())

            elif choice == "3":
                print("\nрезультат пошуку")
                found = self.service.get_summer_students_3rd_course()
                if not found:
                    print("нікого не знайдено.")
                for s in found:
                    print(s.get_info())

            elif choice == "4":
                break