#Layyana Junaid BS AI - 3A
# Lab 2 , task 2


def checkingLastCharacter():
 
    user = input("Enter a string of characters: ").strip()

    if not user:
        print("The input string is empty.")
        return  

    vowels = "aeiouAEIOU"

    lastChar = user[-1]

    if lastChar in vowels:
        print(f"The last letter '{lastChar}' is a vowel.")
    elif lastChar.isalpha():
        print(f"The last letter '{lastChar}' is a consonant.")
    else:
        print(f"The last character '{lastChar}' is not an alphabetic letter.")

# Example usage
checkingLastCharacter()
