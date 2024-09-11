#Layyana Junaid 23k-0056
#Lab04 task 1

#using zip function to join lists

a = ["He", "th", "i", "Sal"]
b = ["llo", "is", "s", "man"]

c = [x + y for x, y in zip(a, b)]

print(list(c))