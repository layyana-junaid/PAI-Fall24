#Layyana Junaid 23k-0056
#Lab 4 task 3

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_biodata(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


obj1 = Student('Layyana', 20)
obj1.print_biodata()

obj2 = Student('Amna' , 19)
obj2.print_biodata()
        