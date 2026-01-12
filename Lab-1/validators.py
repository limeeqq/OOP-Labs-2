import re

class Validator:
    @staticmethod
    def is_name(value):
        #тільки кирилиця або латиниця
        return bool(re.match(r"^[a-zA-Zа-яА-ЯіІїЇєЄ]+$", value))

    @staticmethod
    def is_ticket(value):
        # 2літ 4 цифри
        return bool(re.match(r"^[A-ZА-Я]{2}\d{6}$", value))

    @staticmethod
    def is_date(value):
        # день місяць рік
        return bool(re.match(r"^\d{2}-\d{2}-\d{4}$", value))