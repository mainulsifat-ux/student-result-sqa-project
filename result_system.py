class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks < 0 or self.marks > 100:
            raise ValueError("Marks must be between 0 and 100")

        if self.marks >= 80:
            return "A+"
        elif self.marks >= 70:
            return "A"
        elif self.marks >= 60:
            return "A-"
        elif self.marks >= 50:
            return "B"
        elif self.marks >= 40:
            return "C"
        else:
            return "F"


def main():
    print("Student Result Management System")

    name = input("Enter student name: ")
    marks = int(input("Enter marks (0-100): "))

    student = StudentResult(name, marks)
    grade = student.calculate_grade()

    print("\n----- Result -----")
    print("Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)


if __name__ == "__main__":
    main()
