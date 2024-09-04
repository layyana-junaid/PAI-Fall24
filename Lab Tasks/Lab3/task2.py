#Layyana Junaid BSAI-3A
#Lab 3 task2

try:
    file = open("task2.txt", "w")
    file.write("Hello I am Layyana, Hello")
    file.close()

except:
    print("File was unable to create.")


file = open("task2.txt", "r")
try:
    data = file.read()
    data = data.replace("Hello", "HI!")
    file.close()

except:
    print("Hello doesn't exist in the file.")

with open("task2.txt", "w") as file:
    file.write(data)
