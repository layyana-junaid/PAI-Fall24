#Layyana Junaid 23k-0056 BsAi- 3A
#Lab 3 task 5

import json


def savejson(filePath, data):
    try:
        with open(filePath, 'w') as file:
            json.dump(data, file)
    except IOError:
        print("IOError: An error occurred while writing to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def loadfromJson(filePath):
    try:
        with open(filePath, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{filePath}' was not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON or cannot be decoded.")
        return {}
    except IOError:
        print("IOError: An error occurred while reading the file.")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}


def findMaxAge(data):
    try:
        if not data:
            raise ValueError("The dictionary is empty.")
        max_age = max(data.values())
        persons_with_max_age = [name for name, age in data.items() if age == max_age]

        print(f"Person(s) with the maximum age ({max_age}): {', '.join(persons_with_max_age)}")

        age_count = {}
        for age in data.values():
            if age in age_count:
                age_count[age] += 1
            else:
                age_count[age] = 1

        duplicates = {age for age, count in age_count.items() if count > 1}
        if duplicates:
            print(f"Duplicate ages found: {', '.join(map(str, duplicates))}")
        else:
            print("No duplicate ages found.")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    dictionary = {'Ali': 23, 'Saad': 24, 'Salman': 15, 'Shams': 25, 'Sadiq': 46, 'Hammad': 23}
    try:
        while True:
            name = input("Enter name (or type 'done' to finish): ")
            if name.lower() == 'done':
                break
            age = int(input(f"Enter age for {name}: "))
            dictionary[name] = age

        filePath = 'employee_data.json'
        savejson(filePath, dictionary)
        loaded_dict = loadfromJson(filePath)
        findMaxAge(loaded_dict)

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

main()
