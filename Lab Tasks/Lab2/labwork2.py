#Layyana Junaid BS AI - 3A
# Lab 2 , task 2

# taking a string as a user input and then checking about the vowel
def CheckingLastCharacter() :
    user = input("Enter a string of characters: ").strip()

    if not user:
       print("String is empty")


    vowels = "aeiouAEIOU"

    # Get the last character of the string
    last_char = user[-1]
    if last_char in vowels:
       print(f"The last letter '{last_char}' is a vowel.")
    else:
       print(f"The last letter '{last_char}' is a consonant.")