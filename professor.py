from person import Person
from course import Course
class Professor(Person):
    def __init__(self, first_name, last_name, dob, phone, address, salary):
        super().__init__(self, first_name, last_name, dob, phone, address)
        self.salary = salary
        self.courses = []
        self.got_raise = False  # used to prevent giving raise multiple times when len(self.courses) >= 4

    def check_for_raise(self):
        if len(self.courses) >= 4 and not self.got_raise:
            self.salary += 20000
            self.got_raise = True

    def add_course(self, course):
        if not isinstance(course, Course):
            raise Exception("Invalid Course! Provide instance of the class Course.")
        self.courses.append(course)