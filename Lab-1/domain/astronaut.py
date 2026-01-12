from .person import Person

class Astronaut(Person):
    def __init__(self, first_name, last_name, rank):
        super().__init__(first_name, last_name)
        self.rank = rank

    def get_info(self):
        return f"Astronaut: {self.first_name} {self.last_name}, Rank: {self.rank}"