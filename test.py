"""This module provides the structure that represents the Student entity and
the operations that are performed on its data. It also provides the functionality
to create a quick test run that demonstrates the instation of an object and performing
operations on it."""
import numbers


class Student:
    """_summary_
    """
    def __init__(self, student_id: str, name: str):
        """Initializes a Student object.

        Args:
            student_id (str): Unique ID for the student.
            name (str): Name of the student.
        """
        if not (student_id and name):
            print("ID and name must not be empty.")
            return
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = False
        self.letter = "n/a"

    def add_grades(self, grade: float):
        """Registers a new grade for the student.

        Args:
            grade (float): A decimal number between 0 and 10.
        """
        if not isinstance(grade, numbers.Number):
            print("The input is not a number.")
            return
        if not 0 <= grade <= 100:
            print("The input is not between 0 and 100.")
            return
        self.grades.append(grade)

    def calc_average(self):
        """Calculates the average grade for the student.

        Returns:
            float: A decimal number between 0 and 10.
        """
        definitions = {
            "A": [90, 100],
            "B": [80, 89],
            "C": [70, 79],
            "D": [60, 69],
            "F": [0, 59]
        }
        t = 0
        for x in self.grades:
            t += x
        avg = t / len(self.grades)
        for letter, interval in definitions.items():
            if interval[0] <= avg <= interval[1]:
                self.letter = letter
                break
        return avg

    def check_honor(self):
        """Flags the student as part of the Honor Roll if it passes a grade check.
        """
        if self.calc_average() > 90:
            self.honor = True

    def delete_grade(self, value: float=-1, index: int=-1):
        """Removes the grade at the received index, if it exists.

        Args:
            value (float): _description_
            index (int): _description_
        """
        if value >= 0:
            if value <= 100:
                try:
                    index = self.grades.index(value)
                except ValueError:
                    print("The specified value does not exist in the list.")
                    return
            else:
                print("Invalid value.")
                return
        if not index:
            print("Missing index.")
            return
        if  index < 0 or index > len(self.grades):
            print("Index out of bounds.")
            return
        del self.grades[index]
    def determine_pass(self):
        """Flags the student as passed or failed.
        """
        avg = self.calc_average()
        if avg > 60:
            self.is_passed = True

    def report(self):
        """Print a report with the student's attributes.
        """
        print("ID: " + self.student_id)
        print("Name is: " + self.name)
        print(f"Grades Count: {len(self.grades)}")
        print("Final Grade = " + self.letter)
        print(f"Passed = {self.is_passed}")
        print(f"In honor roll = {self.honor}")


def start_run():
    """Runs a mock student test.
    """
    a = Student("x", "Test")
    if not a:
        print("Could not create the student.")
        return
    a.add_grades(100)
    a.add_grades("Fifty")
    a.calc_average()
    a.check_honor()
    a.delete_grade(5)
    a.report()


start_run()
