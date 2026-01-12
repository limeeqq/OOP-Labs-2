from database import Database
from validators import Validator
from domain.student import Student
from domain.teacher import Teacher
from domain.astronaut import Astronaut

class ConsoleMenu:
    def __init__(self):
        self.db = Database()
        self.people = []

    def start(self):
        while True:
         
            print("\n Головне меню")
            print("1. Додати студента")
            print("2. Додати викладача")
            print("3. Додати астронавта")
            print("4. Показати всіх")
            print("5. Зберегти дані")
            print("6. Завантажити дані")
            print("7. Пошук")
            print("0. Вихід")
            
            choice = input("Введть цифру: ")

            if choice == '1': self.add_student()
            elif choice == '2': self.add_teacher()
            elif choice == '3': self.add_astronaut()
            elif choice == '4': self.show_all()
            elif choice == '5': self.db.save(self.people)
            elif choice == '6': 
                self.people = self.db.load()
                print("Дані завантажено")
            elif choice == '7': self.task_variant_1()
            elif choice == '0': break
            else: print("Невірно, спробуйте ще раз")

    def add_student(self):
        print("\nНовий Студент!")
        fn = self._ask("Ім'я: ", Validator.is_name)
        ln = self._ask("Прізвище: ", Validator.is_name)
        
        while True:
            try:
                cr = int(input("Курс 1-6: "))
                if 1 <= cr <= 6: break
            except: pass
            print("помилка! курс має бути числом від 1 до 6")

        tk = self._ask("студентський, приклад = KB123456 : ", Validator.is_ticket)
        bd = self._ask("дата народження приклад=(ДД-ММ-РРРР): ", Validator.is_date)
        
        self.people.append(Student(fn, ln, cr, tk, bd))
        print("-> студент доданий.")

    def add_teacher(self):
        print("\nНовий викладач")
        fn = self._ask("Ім'я: ", Validator.is_name)
        ln = self._ask("Прізвище: ", Validator.is_name)
        sb = input("Предмет: ")
        self.people.append(Teacher(fn, ln, sb))
        print("-> Викладач доданий")

    def add_astronaut(self):
        print("\nНовий Астронавт")
        fn = self._ask("Ім'я: ", Validator.is_name)
        ln = self._ask("Прізвище: ", Validator.is_name)
        rk = input("Звання: ")
        self.people.append(Astronaut(fn, ln, rk))
        print("-> Астронавт доданий")

    def show_all(self):
        if not self.people:
            print("список порожній")
            return
        
        print("\n   список користувачів")
        for p in self.people:
            print(p.get_info())
            if isinstance(p, Student):
                print(f"   * {p.sing()}") 

    def task_variant_1(self):
        """Студенти 3 курсу, народжені влітку: """
        print("\nРезультати пошуку (3 курс або літо)")
        found = False
        for p in self.people:
            if isinstance(p, Student) and p.course == 3:
                try:
                    parts = p.birth_date.split('-')
                    month = int(parts[1])
                    if 6 <= month <= 8:
                        print(p.get_info())
                        found = True
                except:
                    continue
        
        if not found:
            print("нікого не знайдено.")

    def _ask(self, prompt, validator_func):
        while True:
            value = input(prompt)
            if validator_func(value):
                return value
            print("невірний формат, спробуйте ще раз")