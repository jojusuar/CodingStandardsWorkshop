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
        self.honor = False
        self.letter = "N/A"

    def add_grades(self, g):
        """
        This method adds a grade to the grades list
        """
        if not isinstance(g, int):
            print("Error: Grade must be an integer")
            return

        if g < 0 and g > 100:
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
            self.honor = True

    def delete_grade(self, index):
        """
        This method removes grade from list
        """
        if len(self.grades) < index:
            print("Error: Index out of range")
            return
        del self.grades[index]

    def report(self):
        """
        This method prints out all student information
        """
        print("ID: " + str(self.id))
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.grades)))
        print("Grades: " + str(self.grades))
        print("Average Grade = " + str(self.calc_average()))
        print("Final Grade = " + self.letter)
        print("Honor Roll: " + str(self.honor))
        print("Passed: " + self.is_passed)

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

    def has_passed(self):
        """
        This method checks if student passed
        """
        if self.calc_average() >= 60:
            self.is_passed = "YES"
        else:
            self.is_passed = "NO"


def start_run():
    """
    This method runs all method at once
    """
    a = Student(1, "Nombre")
    a.add_grades(100)
    a.calc_average()
    a.check_honor()
    a.has_passed()
    a.calculate_letter()
    a.report()


start_run()
