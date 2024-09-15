#Layyana Junaid 23k-0056
#Lab 09 task 9

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")


class Marks(Student):
    def __init__(self, student_id, name, marks_algo, marks_dataScience, marks_calculus):
        super().__init__(student_id, name)
        self.marks_algo = marks_algo
        self.marks_dataScience = marks_dataScience
        self.marks_calculus = marks_calculus

    def display_marks(self):
        print(f"Algorithm Marks: {self.marks_algo}")
        print(f"Data Science Marks: {self.marks_dataScience}")
        print(f"Calculus Marks: {self.marks_calculus}")


class Result(Marks):
    def __init__(self, student_id, name, marks_algo, marks_dataScience, marks_calculus):
        super().__init__(student_id, name, marks_algo, marks_dataScience, marks_calculus)

    def calculate_total_and_average(self):
        total_marks = self.marks_algo + self.marks_dataScience + self.marks_calculus
        average_marks = total_marks / 3
        return total_marks, average_marks

    def display_result(self):
        self.display_info()
        self.display_marks()
        total_marks, average_marks = self.calculate_total_and_average()
        print(f"Total Marks: {total_marks}")
        print(f"Average Marks: {average_marks:.2f}")


student_result = Result(student_id=101, name="Layyana Junaid", marks_algo=85, marks_dataScience=90, marks_calculus=78)
student_result.display_result()
