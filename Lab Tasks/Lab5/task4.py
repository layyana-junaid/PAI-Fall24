#Layyana Junaid 23k-0056 BSAI-3A
#task 4

class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def students_info(self):
        print(f"Students Name: {self.name}")
        print(f"Students ID: {self.id}")

class Marks(Student):
    def __init__(self, marks_algo, marks_dataScience, marks_calculus, name, id):
        super().__init__(name, id)
        self.marks_algo = marks_algo
        self.marks_dataScience = marks_dataScience
        self.marks_calculus = marks_calculus

    def students_marks(self):
        print(f"Marks in Algorithm: {self.marks_algo}")
        print(f"Marks in Data Science: {self.marks_dataScience}")
        print(f"Marks in Calculus: {self.marks_calculus}")

class Result(Marks):
    def __init__(self, marks_algo, marks_dataScience, marks_calculus, name, id):
        super().__init__(marks_algo, marks_dataScience, marks_calculus, name, id)

    def average_marks(self):
        total = self.marks_calculus + self.marks_algo + self.marks_algo
        avg = total / 3

        print(f"Total Marks Obtained: {total}")
        print(f"Average Marks Obtained: {avg}")

s1 = Student("Layyana Junaid", 230056)
s1.students_info()

m1 = Marks(75, 80, 70, "Layyana", 230056)
m1.students_marks()

r1=Result(75, 80, 70, "Layyana", 230056)
r1.average_marks()



