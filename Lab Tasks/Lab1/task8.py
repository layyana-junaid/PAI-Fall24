#Layyana Junaid (23k-0056)
#using for loop to iterate numbers and classify it

for i in range(1, 51):
    if i % 3 == 0 :
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i) # if not and than print the number itself