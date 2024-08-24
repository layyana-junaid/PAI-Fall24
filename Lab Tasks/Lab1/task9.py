#Layyana Junaid (23k-0056)
#creating a multiplication table for 1 - 10
# taking input of the number from the user

num = int(input("Enter the number for which you want a multiplication table: "))

for i in range(1 ,11):
    print(f"{num} x {i} = {num * i}")