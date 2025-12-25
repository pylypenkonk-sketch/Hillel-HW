import zipfile

# Створимо zip-файл
with zipfile.ZipFile('student_project.zip', 'w') as zipf:
    # Додаємо human.py
    zipf.writestr('human.py', """
class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} років, {self.gender}"
""")

    # Додаємо student.py
    zipf.writestr('student.py', """
from human import Human

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Заліковка: {self.record_book}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return str(self) == str(other)
        return False

    def __hash__(self):
        return hash(str(self))
""")

    # Додаємо exceptions.py
    zipf.writestr('exceptions.py', """
class GroupLimitError(Exception):
    def __init__(self, message="У групі не може бути більше 10 студентів"):
        self.message = message
        super().__init__(self.message)
""")

    # Додаємо group.py
    zipf.writestr('group.py', """
from exceptions import GroupLimitError

class Group:
    def __init__(self, number, max_students=10):
        self.number = number
        self.group = set()
        self.max_students = max_students

    def add_student(self, student):
        if len(self.group) >= self.max_students:
            raise GroupLimitError(f"Неможливо додати {student.last_name}. Межа {self.max_students} осіб!")
        self.group.add(student)

    def find_student(self, last_name):
        return next((s for s in self.group if s.last_name == last_name), None)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __len__(self):
        return len(self.group)

    def __str__(self):
        all_students = '\\n'.join(str(student) for student in self.group)
        return f'Група: {self.number}\\nКількість: {len(self)}\\nСтуденти:\\n{all_students}'
""")

    # Додаємо main.py
    zipf.writestr('main.py', """
from student import Student
from group import Group

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

print(gr)

assert gr.find_student('Jobs') == st1
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr)  # Only one student
""")

print("student_project.zip створено успішно!")

print(f"Zip-файл створено за адресою: {full_path}")
