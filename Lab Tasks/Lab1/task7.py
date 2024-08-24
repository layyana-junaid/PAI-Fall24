#Layyana Junaid (23k-0056)
# a program that takes in a string input and the reverses it

word = input("Enter a word you want to reverse: ")

reverseWord = '' # making an empty string to store the reversed string

for i in range(len(word)-1, -1, -1):
    reverseWord += word[i]

print("Revered String: ", reverseWord)