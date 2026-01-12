from domain.student import Student
from domain.teacher import Teacher
from domain.astronaut import Astronaut

class Database:
    def __init__(self, filename="database.txt"):
        self.filename = filename

    def save(self, people_list):
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                for p in people_list:
                    full_name = f"{p.first_name}{p.last_name}"
                    
                    if isinstance(p, Student):
                        f.write(f"Student {full_name}\n{{\n")
                        f.write(f'    "firstname": "{p.first_name}",\n')
                        f.write(f'    "lastname": "{p.last_name}",\n')
                        f.write(f'    "course": "{p.course}",\n')
                        f.write(f'    "ticket": "{p.ticket}",\n')
                        f.write(f'    "birthdate": "{p.birth_date}"\n')
                        f.write("};\n")
                    
                    elif isinstance(p, Teacher):
                        f.write(f"Teacher {full_name}\n{{\n")
                        f.write(f'    "firstname": "{p.first_name}",\n')
                        f.write(f'    "lastname": "{p.last_name}",\n')
                        f.write(f'    "subject": "{p.subject}"\n')
                        f.write("};\n")
                    
                    elif isinstance(p, Astronaut):
                        f.write(f"Astronaut {full_name}\n{{\n")
                        f.write(f'    "firstname": "{p.first_name}",\n')
                        f.write(f'    "lastname": "{p.last_name}",\n')
                        f.write(f'    "rank": "{p.rank}"\n')
                        f.write("};\n")
            print("Дані успішно збережено")
        except Exception as e:
            print(f"Помилка збереження {e}")

    def load(self):
        people = []
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                lines = [line.strip() for line in f.readlines()]
            
            i = 0
            while i < len(lines):
                line = lines[i]
                
                if line.startswith("Student"):
                    fn = self._get_val(lines[i+2])
                    ln = self._get_val(lines[i+3])
                    cr = int(self._get_val(lines[i+4]))
                    tk = self._get_val(lines[i+5])
                    bd = self._get_val(lines[i+6])
                    people.append(Student(fn, ln, cr, tk, bd))
                    i += 7 
                elif line.startswith("Teacher"):
                    fn = self._get_val(lines[i+2])
                    ln = self._get_val(lines[i+3])
                    sb = self._get_val(lines[i+4])
                    people.append(Teacher(fn, ln, sb))
                    i += 5
                
                elif line.startswith("Astronaut"):
                    fn = self._get_val(lines[i+2])
                    ln = self._get_val(lines[i+3])
                    rk = self._get_val(lines[i+4])
                    people.append(Astronaut(fn, ln, rk))
                    i += 5
                
                else:
                    i += 1
            
            return people
        except FileNotFoundError:
            return []

    def _get_val(self, line):
        parts = line.split('"')
        if len(parts) >= 4:
            return parts[3]
        return ""