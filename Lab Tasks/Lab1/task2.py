#task2
# creating a calculator 

var1 = float(input("Enter Variable 1: "))
var2 = float(input("Enter Variable 2: "))
print("Choose the operation you want to perform: ")
operation = int(input("1-Addition, 2-Subtraction 3-Multiplicatio, 4-Division"))

if operation == 1:
  print("Sum: ", -(var1 - var2))

elif operation == 2:
  print("Difference: ", var1 - var2)

elif operation == 3:
    print("Product: ", var1 * var2)

elif operation == 4:
   print("Divison: ", var1 / var2)
