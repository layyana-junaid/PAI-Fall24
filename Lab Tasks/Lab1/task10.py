#Layyana Junaid (23k-0056)
#finding the largest number in a user input list

NumbList = []
num = int(input("How many numbers you want to add: "))

for _ in range(num):
    userInput = int(input("Enter number: "))
    num = int(userInput)
    NumbList.append(num)

largestNum = NumbList[0]

for num in NumbList:
    if num > largestNum:
        largestNum = num

print("The largest number in the list is: ", largestNum)
