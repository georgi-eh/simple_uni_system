from person import Person
from enroll import Enroll


class Student(Person):
    def __init__(self, first_name, last_name, dob, phone, address, international=False):
        super().__init__(self, first_name, last_name, dob, phone, address)
        self.international = international
        self.enrolls = []  # all courses in which the student is enrolled

    def add_enroll(self, course):
        if not isinstance(course, Enroll):
            raise Exception("Invalid Enroll! Provide instance of the class Enroll.")
        self.enrolls.append(course)

        def is_on_probation(self):
            return False

        def is_part_time(self):
            return len(self.enrolls) <= 3  # if student participates in more than 3 classes, he/she is full time


