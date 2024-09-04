#Layyana Junaid BSAI-3A
#Lab 3 task1

#using txt file
try:
    file = open("task.txt", "w")
    file.write("My name is Layyana")
    file.close()

except FileExistsError:
    print("The file already exists")

try: 
    with open("task.txt", "r") as file:
        data = file.read()

    print("The Character count is: ", len(data))

except FileNotFoundError: 
    print("The file was not found.")

#using jason file
import json

def countCharacters(filePath):
    try:
        with open(filePath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            text = data.get('text', '')
            charCount = len(text)
            wordCount = len(text.split())
            
            print(f"Total number of characters: {charCount}")
            print(f"Total number of words: {wordCount}")
    
    except FileNotFoundError:
        print(f"Error: The file '{filePath}' does not exist.")
    except IOError:
        print("Error: An IOError occurred while reading the file.")
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON or cannot be decoded.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

filePath = 'data.json'
countCharacters(filePath)
   
























