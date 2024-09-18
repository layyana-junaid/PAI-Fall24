#Layyana Junaid 23k-0056 BSAI-3A
#task 6

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        raise NotImplementedError("---Bonus Calculating---")


class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.2

    def hire(self):
        print(f"{self.name} is hiring someone.")


class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.1

    def write_code(self):
        print(f"{self.name} is writing code.")


class SeniorManager(Manager):
    def calculate_bonus(self):
        return self.salary * 0.3


m1 = Manager("Layyana", 50000)
bonus = m1.calculate_bonus()
print(f"Manager bonus: {bonus}")

m1 = Manager("Layyana", 50000)
m1.calculate_bonus()
m1.hire()

d1 = Developer("Layyana", 50000)
d1.calculate_bonus()
d1.write_code()