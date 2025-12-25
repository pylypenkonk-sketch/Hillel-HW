class GroupLimitError(Exception):
    """Власний клас помилки для обмеження кількості студентів"""
    def __init__(self, message="У групі не може бути більше 10 студентів"):
        self.message = message
        super().__init__(self.message)

class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} років, {self.gender}"

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Заліковка: {self.record_book}"

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
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Група: {self.number}\nКількість: {len(self)}\nСтуденти:\n{all_students}'

st1 = Student('Чоловік', 30, 'Стів', 'Джобс', 'AN142')
st2 = Student('Жінка', 25, 'Ліза', 'Тейлор', 'AN145')

gr = Group('PD1')

try:
    gr.add_student(st1)
    gr.add_student(st2)
    print(gr)
    print(f"Пошук Джобса: {gr.find_student('Jobs')}")
except GroupLimitError as e:
    print(e)

print("Перевірка завершена успішно")