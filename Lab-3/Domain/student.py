from datetime import datetime

class Student:
    def __init__(self, last_name, first_name, course, ticket, birth_date_str, group_num):
        self.last_name = last_name
        self.first_name = first_name
        self.course = int(course)
        self.ticket = ticket
        self.birth_date_str = birth_date_str  # формат дата місяць рік
        self.group_num = group_num

    def get_info(self):
        return (f"{self.last_name} {self.first_name}, Група: {self.group_num}, "
                f"Курс: {self.course}, ДН: {self.birth_date_str}")

    def get_age(self):
        try:
            b_date = datetime.strptime(self.birth_date_str, "%d-%m-%Y")
            today = datetime.now()
            return today.year - b_date.year - ((today.month, today.day) < (b_date.month, b_date.day))
        except ValueError:
            return 0

    def is_born_in_summer(self):
        try:
            b_date = datetime.strptime(self.birth_date_str, "%d-%m-%Y")
            # місяці літа
            return b_date.month in [6, 7, 8]
        except ValueError:
            return False

    def to_dict(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "course": self.course,
            "ticket": self.ticket,
            "birth_date_str": self.birth_date_str,
            "group_num": self.group_num
        }

    @staticmethod
    def from_dict(data):
        return Student(
            data["last_name"],
            data["first_name"],
            data["course"],
            data["ticket"],
            data["birth_date_str"],
            data["group_num"]
        )