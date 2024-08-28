#Layyana Junaid BSAI - 3A
#task 6

def Multiply(numbers):
    result = 1;
    for number in numbers: 
        result *= number

    return result 

numbers = [2 , 3, 4, 5, 6]
print(f"Product of List: {Multiply(numbers)}")