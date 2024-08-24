#Layyana Junaid (23k-0056)
#creating a list and taking input from the user

Lists = []
for i in range(0, 10, 1):
    l = int(input("Enter the elements in list: "))
    Lists.append(l)
print(Lists)

#enter the number which will be checked and anything below it will be removed
numb = int(input("Enter the number: "))

#evaluating filtered list
filter = (num for num in Lists if num >= numb)
filteredList = list(filter)

print("Filtered List(Elements greater than or equal to the", numb,  "): ", filteredList)



