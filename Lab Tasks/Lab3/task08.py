#Layyana Junaid 23k-0056 BSAI-3A
#Lab 3 task 8

try:
    num1 = int(input("Enter Integer 1: "))
    num2 = int(input("Enter Integer 2: "))

    if num1 > 0:
        try:
            result = num2 / num1
            print(f"Division of {num2} by {num1} : {result}")
        except ZeroDivisionError:
            print("ZeroDivisonError Occured!")
    else:
        print("First number must be greater than zero")
except ValueError:
    print("ValueError! Input is not an integer")