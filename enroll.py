from course import Course
from student import Student
from datetime import datetime


class Enroll:
    def __init__(self, student, course):
        if not isinstance(student, Student):
            raise Exception("Invalid Student! Provide instance of the class Student.")
        if not isinstance(course, Course):
            raise Exception("Invalid Course! Provide instance of the class Course.")

        self.student = student
        self.course = course
        self.grade = None
        self.date = datetime.now()

    def set_grade(self, grade):
        self.grade = grade
