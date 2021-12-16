"""
A software academy teaches two types of courses: local courses that are held in some of the academy’s local labs
and offsite courses held in some other town outside of the academy’s headquarters. Each course has a name,
a teacher assigned to teach it and a course program (sequence of topics). Each teacher has a name and knows
the courses he or she teaches. Both courses and teachers could be printed in human-readable text form. All your
courses should implement ICourse. Teachers should implement ITeacher. Local and offsite courses should implement
ILocalCourse and IOffsiteCourse respectively. Courses and teachers should be created only through the ICourseFactory
interface implemented by a class named CourseFactory. Write a program that will form courses of software academy.
"""

from abc import abstractmethod, ABC
import json

JSON_FILE_COURSE = "course.json"
JSON_FILE_TEACHER = "teacher.json"


class ICourse(ABC):

    @abstractmethod
    def out_of_json(self):
        pass

    @abstractmethod
    def to_json(self, type_of: str):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def teacher(self):
        pass

    @property
    @abstractmethod
    def course_program(self):
        pass


class ITeacher(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def courses(self):
        pass

    @property
    @abstractmethod
    def add_course(self):
        pass

    @property
    @abstractmethod
    def to_json(self):
        pass


class ILocalCourse(ABC):

    @abstractmethod
    def __str__(self): pass


class IOffsiteCourse(ABC):

    @abstractmethod
    def __str__(self): pass


class ICourseFactory(ABC):

    @abstractmethod
    def course_factory(self, name: str, course_program: list, course_type: str, teacher: ITeacher):
        pass

    @abstractmethod
    def teacher_factory(self, name: str):
        pass

    @abstractmethod
    def delete_course(self, course: ICourse):
        pass


class Course(ICourse):

    def __init__(self, name, course_program, teacher):
        self.name = name
        self.course_program = course_program
        self.teacher = teacher

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError
        if not value.rstrip():
            raise ValueError
        self.__name = value

    @property
    def course_program(self):
        return self.__course_program

    @course_program.setter
    def course_program(self, value):
        if not isinstance(value, list):
            raise TypeError
        if not all(isinstance(t, str) for t in value):
            raise ValueError
        self.__course_program = value

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, value):
        if not isinstance(value, Teacher):
            raise TypeError
        self.__teacher = value

    def to_json(self, type_at):
        exists = False
        t2 = dict()
        with open(JSON_FILE_COURSE, "r") as f:
            data = json.load(f)
        for t in data:
            if t["name"] == self.name and t["teacher"] == self.teacher.name:
                exists = True
                break
        if exists:
            t["type"] = type_at
            t["program"] = self.course_program
            t["teacher"] = self.teacher.name
            with open(JSON_FILE_COURSE, "w") as f:
                json.dump(data, f, indent=4)
        else:
            t2["name"] = self.name
            t2["type"] = type
            t2["program"] = self.course_program
            t2["teacher"] = self.teacher.name
            data.append(t2)
            with open(JSON_FILE_COURSE, "w") as f:
                json.dump(data, f, indent=4)

    def out_of_json(self):
        with open(JSON_FILE_COURSE, "r") as f:
            data = json.load(f)
            for t in data:
                if t["name"] == self.name:
                    json.pop(t)
        with open(JSON_FILE_COURSE, "w") as f:
            json.dump(data, f, indent=4)

    def __str__(self) -> str:
        return f'Course:' \
               f'\n\tname - {self.__name}' \
               f'\n\tteacher - {self.__teacher.name}' \
               f'\n\tprogram - {self.__course_program}'


class Teacher(ITeacher):

    def __init__(self, name):
        self.name = name
        self.courses = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError
        if not value.rstrip():
            raise ValueError
        self.__name = value

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        if not isinstance(value, list):
            raise TypeError
        self.__courses = value

    def add_course(self, name):
        if name in self.courses:
            pass
        else:
            self.courses.append(name)

    def to_json(self):

        exists = False
        with open(JSON_FILE_TEACHER, "r") as f:
            data = json.load(f)
        for teacher in data:
            if teacher["name"] == self.name:
                exists = True
                break
        if exists:
            teacher["courses"] = self.courses
            with open(JSON_FILE_TEACHER, "w") as t:
                json.dump(data, t, indent=4)
        else:
            new_course["name"] = self.name
            new_course["courses"] = self.courses
            data.append(new_course)
            with open(JSON_FILE_TEACHER, "w") as t:
                json.dump(data, t, indent=4)

    def __str__(self):
        return f'Teacher:' \
               f'\n\tname - {self.__name}' \
               f'\n\tcourses - {self.__courses}'


class LocalCourse(Course, ILocalCourse):

    def __init__(self, name, program, teacher):
        super().__init__(name, program, teacher)
        super().to_json("local")

    def delete(self):
        super().out_of_json()

    def __str__(self) -> str:
        return super().__str__() + \
               f'\n\tLocal'


class OffsiteCourse(Course, IOffsiteCourse):

    def __init__(self, name, program, teacher):
        super().__init__(name, program, teacher)
        super().to_json("offsite")

    def delete(self):
        super().out_of_json()

    def __str__(self) -> str:
        return super().__str__() + \
               f'\n\tOffsite'


class CourseFactory(ICourseFactory):

    def course_factory(self, name, course_program, course_type, teacher):
        if course_type == 'local':
            a = LocalCourse(name, course_program, teacher)
        elif course_type == 'offsite':
            a = OffsiteCourse(name, course_program, teacher)
        else:
            raise ValueError("Error! Incorrect value!")
        teacher.add_course(name)
        teacher.to_json()
        return a

    def teacher_factory(self, name):
        with open(JSON_FILE_TEACHER, "r") as file_teacher:
            teachers = json.load(file_teacher)
        for t in teachers:
            if name == t["name"]:
                teacher = Teacher(t["name"])
                teacher.courses.extend(t["courses"])
                return teacher
            else:
                return Teacher(name)

    def delete_course(self, course):
        del course


new_course = CourseFactory()
new_teacher = new_course.teacher_factory("Vladislav Volodymirovich")
new_teacher2 = new_course.teacher_factory("Dima")
new_course2 = new_course.course_factory("Better Code Python", ["1st step", "2nd step"], "local", new_teacher)
new_course3 = new_course.course_factory("Better Code Python", ["1st step", "2nd step", "3rd step", "finish"],
                                        "offsite", new_teacher)
print(new_course2)
print(new_course3)
