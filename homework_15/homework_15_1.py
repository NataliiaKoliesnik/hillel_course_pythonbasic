# classes and custom exception handling

class GroupLimitError(Exception):
    pass

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.gender}, {self.age}, {self.first_name}, {self.last_name}'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()}, {self.record_book}'

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError('A group cannot contain more than 10 students')
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student is not None:
            self.group.discard(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students = f'{all_students}{str(student)}; '
        return f'Number:{self.number}\n {all_students} '

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Female', 24, 'Nina', 'Abramova', 'AN145')
st4 = Student('Male', 35, 'Sergiy', 'Kozachenko', 'AN142')
st5 = Student('Male', 23, 'Alex', 'Dril', 'AN142')
st6 = Student('Female', 25, 'Lilya', 'Tkachuk', 'AN145')
st7 = Student('Female', 24, 'Vera', 'Andrushenko', 'AN145')
st8 = Student('Female', 27, 'Mila', 'Milkevich', 'AN145')
st9 = Student('Female', 28, 'Mariya', 'Bondar', 'AN145')
st10 = Student('Female', 32, 'Irina', 'Ohrimchuk', 'AN142')
st11 = Student('Male', 33, 'Bogdan', 'Gonchar', 'AN142')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
gr.add_student(st11)
print(gr)