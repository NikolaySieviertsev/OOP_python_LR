"""
Task 3.
The class GROUP contains a sequence of instances of the class STUDENT. The class STUDENT contains
the student's name, surname, record book number and grades. Determine the required attributes-data
and attributes-methods in classes GROUP and STUDENT. Find the average score of each student. Output
to the standard output stream the five students with the highest average score.
Assume that there can be no more than 20 students in a group, as well as students with the same name and surname.
"""

MAX_AMOUNT_OF_STUDENTS = 20


class Student:
    """ Class Student contains the student's name, surname, record book number and grades.
         Also it has getter and setter methods for appropriate attributes and a method to find average scores."""

    def __init__(self, name, surname, record_book, *grades):
        self.name = name
        self.surname = surname
        self.record_book = record_book
        self.grades = grades

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Surname has to be string type!')
        if not name:
            raise ValueError('Name cannot be empty!')
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError('Surname has to be string type!')
        if not surname:
            raise ValueError('Surname cannot be empty!')
        self.__surname = surname

    @property
    def record_book(self):
        return self.__record_book

    @record_book.setter
    def record_book(self, record_book):
        if not isinstance(record_book, int):
            raise TypeError('Record book number has to be int type! ')
        self.__record_book = record_book

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, grades):
        if not all(isinstance(index, int) for index in grades):
            raise TypeError('Grade have to be int type!')
        if not all(grades):
            raise ValueError('Grades sequence cannot be empty!')
        self.__grades = grades

    @property
    def average_score(self):
        return round(sum(self.grades) / len(self.grades), 1)

    def __str__(self) -> str:
        return f'Name: {self.name}\nSurname: {self.surname}\nRecord book number: {str(self.record_book)}\n' \
               f'Grades: {self.grades}\nAverage: {self.average_score}\n\n'


class Group:
    """" Class Group contains a sequence of instances of the class Student.
          Also it contains list of students and method to find students with the highest average score."""

    def __init__(self, *students):
        self.students = students

    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self, student_list):
        if not student_list:
            raise ValueError('Group cannot be empty!')
        if len(student_list) > MAX_AMOUNT_OF_STUDENTS:
            raise ValueError('Group have to contain less than 20 students!')
        if isinstance(all(student_list), Student):
            raise TypeError('Students have to be "Student" type!')
        if self.duplicates(student_list):
            raise ValueError('Group cannot have students with the same names and surnames!')
        self.__students = list(student_list)

    def best_student(self):
        self.students.sort(key=lambda x: x.average_score, reverse=True)

    @staticmethod
    def duplicates(student_list):
        counter = 0
        names = set()
        for i in student_list:
            names.add(i.name + i.surname)
            counter += 1
        if counter > len(names):
            return True
        return False

    def __str__(self):
        field = ""
        for index in self.students[:5]:
            field += str(index) + "\n"
        return f'{field}'


instance1 = Student('Kolya', 'Severtsev', 1, 5, 1, 5, 2, 5, 5)
instance2 = Student('Max', 'Alexenko', 3, 5, 4, 3, 3, 2, 1)
instance3 = Student('Dima', 'Kashuba', 2, 5, 5, 3, 1, 2, 5)
instance4 = Student('Vlad', 'Leonenko', 4, 1, 5, 3, 3, 2, 1)
instance5 = Student('Oleh', 'Oliynik', 5, 5, 5, 5, 5, 5, 5)
group = Group(instance1, instance2, instance3, instance4, instance5)
group.best_student()
print(group)
# print(instance3)
