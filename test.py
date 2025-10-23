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
        if not isinstance(g, int):
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
        if len(self.grades) < index:
            print("Error: Index out of range")
            return
        del self.grades[index]

    def report(self):  # broken format
        """
        This method prints out all student information
        """
        print("ID: " + str(self.id))
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.grades)))
        print("Final Grade = " + self.letter)

    def calculate_letter(self):
        """
        This method calculates letter grade
        """
        avg = self.calc_average()
        if avg >= 90:
            self.letter = "A"
        elif avg >= 80:
            self.letter = "B"
        elif avg >= 70:
            self.letter = "C"
        elif avg >= 60:
            self.letter = "D"
        else:
            self.letter = "F"


def start_run():
    """
    This method runs all method at once
    """
    a = Student(1, "Nombre")
    a.add_grades(100)
    a.add_grades("Fifty")
    a.calc_average()
    a.check_honor()
    a.calculate_letter()
    a.delete_grade(3)
    a.report()


start_run()
