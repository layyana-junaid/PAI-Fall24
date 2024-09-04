#Layyana Junaid BS AI -3A 23k0056
#Lab 3 task 6

sentence = input("Sentence: ")
with open("questions.txt", "w") as file:
    try:
        if(sentence[len(sentence) - 1] == '?'):
            file.write(sentence)
    except ValueError:
        print("Error: input is not a question")