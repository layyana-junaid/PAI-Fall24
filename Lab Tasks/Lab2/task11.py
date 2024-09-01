#Layyana Junaid 23k-0056 BSAI-3A
#task 11

students = {
    'Layyana' : [80, 90, 75],
    'Alisha' : [85, 70, 90],
    'Hafsa' : [70, 80, 75]
}

def AddGrade(name, grade):
    if name in students:
        students[name].append(grade)
        print(f"Added Grade {grade} for {name}")
    else:
        print(f"Student {name} not found")


def Average(name):
    if name in students:
        grades = students[name]
        if grades:
            average = sum(grades) / len(grades)
            print(f"The average grade for {name} is {average:.2f}.")
        else:
            print(f"{name} has no grades.")
    else:
        print(f"Student {name} not found.")

def addStudent(name):
    if name not in students:
        students[name] = []
        print(f"New student {name} has been added")
    else:
        print(f"{name} already exists")

def removeStudent(name):
    if name in students:
        del students[name]
        print(f"{name} removed from the list")
    else:
        print(f"{name} not found")

AddGrade("Alisha", 70)
Average("Layyana")
addStudent("Abdullah")
addStudent("Layyana")
removeStudent("Hafsa")
