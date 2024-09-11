#Layyana Junaid 23k-0056
#Lab 4 task 4

class Employee:
    #creating a constructor similar to cpp and set default values
    def __init__(self):
        self.name = " "
        self.salary = 0.0
        self.tax = 2.0 
    
    def get_data(self):
        self.name = input("Employee Name: ")
        self.salary = float(input("Employee Salary: "))
        self.tax = float(input("Tax Percentage: "))

    def Salary_after_tax(self):
        after_tax = self.salary * (self.tax / 100)
        salary_after_tax = self.salary - after_tax

        return salary_after_tax
    
    def update_tax_percentage(self, new_tax):
        self.tax = new_tax

        salary_after_tax = self.Salary_after_tax()
        return salary_after_tax
    

employee1 = Employee()
employee1.get_data()

print(f"Salary after tax: ${employee1.Salary_after_tax():.2f}")

new_tax = float(input("Enter new tax percentage: "))
new_salary_after_tax = employee1.update_tax_percentage(new_tax)

print(f"Salary after updated tax: ${new_salary_after_tax:.2f}")