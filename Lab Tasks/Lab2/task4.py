#Layyana Junaid BSAI- 3A
#task 4

def employee(name, salary=10000):
    tax = 0.02
    deductedSalary = salary - (salary * tax)
  
    print(f"Employee Name: {name}")
    print(f"Salary After Tax: {deductedSalary:.2f}")


employee("Laiba")       
employee("Layyana", 30000)  
