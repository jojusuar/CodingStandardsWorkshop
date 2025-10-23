class student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.gradez = []
        self.isPassed = "NO"
        self.honor = "?"
        self.letter = "N/A"  # Initialize letter grade

    def addGrades(self, g):
        # Ensure the grade is a number (int or float)
        if isinstance(g, (int, float)):
            self.gradez.append(g)
        else:
            print(f"Invalid grade {g}: must be a number")

    def calcAverage(self):
        if len(self.gradez) == 0:
            return 0
        t = 0
        for x in self.gradez:
            t += x
        average = t / len(self.gradez)
        # Update letter grade based on average
        if average >= 90:
            self.letter = "A"
        elif average >= 80:
            self.letter = "B"
        elif average >= 70:
            self.letter = "C"
        elif average >= 60:
            self.letter = "D"
        else:
            self.letter = "F"
        return average

    def checkHonor(self):
        if self.calcAverage() > 90:
            self.honor = "yep"

    def deleteGrade(self, index):
        try:
            del self.gradez[index]
        except IndexError:
            print(f"Error: Index {index} is out of range for grades list")

    def report(self):
        print("ID: " + str(self.id))
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.gradez)))
        print("Final Grade = " + self.letter)


def startrun():
    a = student("x", "")
    a.addGrades(100)
    a.addGrades("Fifty")  
    a.calcaverage()
    a.checkHonor()
    a.deleteGrade(5)  
    a.report()


startrun()
