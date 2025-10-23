"""Student Grade Management (console).

Implements Student and StudentManager and a small interactive
console menu to exercise the functionality.
"""
from __future__ import annotations

from typing import Dict, List, Optional, Tuple


class Student:
    """Represents a student and their grades."""

    def __init__(self, id_: str, name: str):
        if not id_ or not isinstance(id_, str) or not id_.strip():
            raise ValueError("ID must be a non-empty string")
        if not name or not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")
        self.id = id_.strip()
        self.name = name.strip()
        self.grades: List[float] = []

    def add_grade(self, value) -> Tuple[bool, str]:
        """Add a grade if numeric and in 0..100.

        Returns (True, message) on success or (False, error) on invalid input.
        """
        try:
            val = float(value)
        except (TypeError, ValueError):
            return False, "Grade must be a number"
        if val < 0 or val > 100:
            return False, "Grade must be between 0 and 100"
        self.grades.append(val)
        return True, "Grade added"

    def calc_average(self) -> Optional[float]:
        """Return average of grades or None if no grades."""
        if not self.grades:
            return None
        return sum(self.grades) / len(self.grades)

    def letter_grade(self) -> Optional[str]:
        """Return letter grade for the current average."""
        avg = self.calc_average()
        if avg is None:
            return None
        if 90 <= avg <= 100:
            return "A"
        if 80 <= avg < 90:
            return "B"
        if 70 <= avg < 80:
            return "C"
        if 60 <= avg < 70:
            return "D"
        return "F"

    def passed(self) -> Optional[bool]:
        """Return True/False depending on average, or None if no grades."""
        avg = self.calc_average()
        if avg is None:
            return None
        return avg >= 60

    def honor_roll(self) -> Optional[bool]:
        """Return True if average >= 90, False if below, or None.
        """
        avg = self.calc_average()
        if avg is None:
            return None
        return avg >= 90

    def remove_grade_by_value(self, value) -> Tuple[bool, str]:
        """Remove the first occurrence of a grade value."""
        try:
            val = float(value)
        except (TypeError, ValueError):
            return False, "Grade must be numeric"
        if val in self.grades:
            self.grades.remove(val)
            return True, "Grade removed by value"
        return False, "Grade value not found"

    def remove_grade_by_index(self, index: int) -> Tuple[bool, str]:
        """Remove a grade at the given index (0-based)."""
        if not isinstance(index, int):
            return False, "Index must be an integer"
        if 0 <= index < len(self.grades):
            del self.grades[index]
            return True, "Grade removed by index"
        return False, "Index out of bounds"

    def summary_report(self) -> str:
        """Return a formatted summary string for this student."""
        avg = self.calc_average()
        avg_str = f"{avg:.2f}" if avg is not None else "N/A"
        letter = self.letter_grade() or "N/A"
        passed = self.passed()
        if passed is None:
            status = "N/A"
        else:
            status = "Passed" if passed else "Failed"
        honor = self.honor_roll()
        honor_str = "Yes" if honor else ("No" if honor is False else "N/A")
        return (
            f"Student ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Number of grades: {len(self.grades)}\n"
            f"Average: {avg_str}\n"
            f"Letter Grade: {letter}\n"
            f"Status: {status}\n"
            f"Honor Roll: {honor_str}"
        )


class StudentManager:
    """Manage students collection and provide operations."""

    def __init__(self) -> None:
        self._students: Dict[str, Student] = {}

    def add_student(self, id_: str, name: str) -> Tuple[bool, str]:
        if not id_ or not isinstance(id_, str) or not id_.strip():
            return False, "ID must not be empty"
        if not name or not isinstance(name, str) or not name.strip():
            return False, "Name must not be empty"
        key = id_.strip()
        if key in self._students:
            return False, "Student with this ID already exists"
        try:
            self._students[key] = Student(key, name.strip())
        except ValueError as exc:
            return False, str(exc)
        return True, "Student added"

    def get_student(self, id_: str) -> Optional[Student]:
        return self._students.get(id_)

    def list_students(self) -> List[Student]:
        return list(self._students.values())


def _prompt_non_empty(prompt: str) -> str:
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("Input must not be empty. Try again.")


def _prompt_grade(prompt: str) -> Optional[float]:
    val = input(prompt).strip()
    try:
        g = float(val)
    except ValueError:
        print("Grade must be numeric")
        return None
    if g < 0 or g > 100:
        print("Grade must be between 0 and 100")
        return None
    return g


def main_menu() -> None:
    mgr = StudentManager()
    menu = (
        "\nStudent Grade System - Menu:\n"
        "1) Add student\n"
        "2) Add grade to student\n"
        "3) Remove grade (by value)\n"
        "4) Remove grade (by index)\n"
        "5) Show student report\n"
        "6) List students\n"
        "7) Exit\n"
    )
    while True:
        print(menu)
        choice = input("Select option: ").strip()
        if choice == "1":
            sid = _prompt_non_empty("Student ID: ")
            name = _prompt_non_empty("Student name: ")
            ok, msg = mgr.add_student(sid, name)
            print(msg)
        elif choice == "2":
            sid = _prompt_non_empty("Student ID: ")
            s = mgr.get_student(sid)
            if not s:
                print("Student not found")
                continue
            g = _prompt_grade("Grade (0-100): ")
            if g is None:
                continue
            ok, msg = s.add_grade(g)
            print(msg)
        elif choice == "3":
            sid = _prompt_non_empty("Student ID: ")
            s = mgr.get_student(sid)
            if not s:
                print("Student not found")
                continue
            val = input("Grade value to remove: ").strip()
            ok, msg = s.remove_grade_by_value(val)
            print(msg)
        elif choice == "4":
            sid = _prompt_non_empty("Student ID: ")
            s = mgr.get_student(sid)
            if not s:
                print("Student not found")
                continue
            idx_raw = input("Index (0-based) to remove: ").strip()
            try:
                idx = int(idx_raw)
            except ValueError:
                print("Index must be integer")
                continue
            ok, msg = s.remove_grade_by_index(idx)
            print(msg)
        elif choice == "5":
            sid = _prompt_non_empty("Student ID: ")
            s = mgr.get_student(sid)
            if not s:
                print("Student not found")
                continue
            print(s.summary_report())
        elif choice == "6":
            students = mgr.list_students()
            if not students:
                print("No students registered")
            for st in students:
                print(f"{st.id}: {st.name} ({len(st.grades)} grades)")
        elif choice == "7":
            print("Bye")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main_menu()
