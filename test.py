"""
This module defines the Student class, which stores basic student information.
"""


class Student:
    """
    This class stores basic student information
    """
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        self.grades = []
        self.is_passed = "NO"
        self.honor = "?"
        self.letter = "N/A"

    def add_grades(self, g):
        """
        This method adds a grade to the grades list
        """
        if g is not int:
            print("Error: Grade must be an integer")
            return
        self.grades.append(g)

    def calc_average(self):
        """
        This method calculates average of grade's list
        """
        t = 0
        for x in self.grades:
            t += x
        return t / len(self.grades)

    def check_honor(self):
        """
        This method calculates if students applies for honor roll
        """
        if self.calc_average() > 90:
            self.honor = "yep"

    def delete_grade(self, index):
        """
        This method removes grade from list
        """
        del self.grades[index]

    def report(self):  # broken format
        """
        This method prints out all student information
        """
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.grades))
        print("Final Grade = " + self.letter)


def start_run():
    """
    This method runs all method at once
    """
    a = Student(1, "Nombre")
    a.add_grades(100)
    a.add_grades("Fifty")  # broken
    a.calc_average()
    a.check_honor()
    a.delete_grade(5)  # IndexError
    a.report()


start_run()
