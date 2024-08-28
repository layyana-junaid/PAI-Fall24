#Layyana Junaid BAI-3A
#====================================================== practise task 1========
# defining functions
var1 = 12
var2 = 2

def add():
    return var1 + var2

def multiply():
    return var1 * var2
def subtract():
    return var1 - var2
def division():
    return var1 / var2

print("====================================================== practise task 1========")
print(add())
print(multiply())
print(subtract())
print(division())

def printGreeting():
    print("Hi, Welcome User!")

printGreeting()

#====================================================== practise task 2========

#making a fucnction to calculate the area of the rectangle


def AreaofRectangle(len, wid):
    area = len * wid
    print(area)

print('====================================================== practise task 2======')
AreaofRectangle(5, 4)

#====================================================== practise task 3========
def find_maximum(*numbers):
    max_value = numbers[0]

    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value
print("====================================================== practise task 3========")
print(find_maximum(3, 5, 7, 2, 8))
print(find_maximum(-1, -5, -3))

#===================================================== practise task 4 =========

#making lambda function for multiplication
multiplication = lambda a = 4, b = 3, c = 2: a * b * c
print(multiplication())