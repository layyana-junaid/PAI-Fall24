#Layyana Junaid BSAI-3A
#Lab 3 task3

def generating_dictionary(keys, values):
    results = {}
    for key, value in zip(keys, values):
        results[key.strip()] = value.strip() 
    return results

def main():
    try:
        input_for_keys = input("Enter elements for the first list (comma separated): ")
        keys = input_for_keys.split(",")

        input_for_values = input("Enter elements for the second list (comma separated): ")
        values = input_for_values.split(",")

        if len(keys) != len(values):
            print("THE LISTS ARE NOT OF THE SAME SIZE!")
            return

        resultant_dict = generating_dictionary(keys, values)

        print("Resultant Dictionary:")
        print(resultant_dict)

        # Write the dictionary to a file:
        with open("dictionary.txt", "w") as file:
            file.write(str(resultant_dict))

        print("Dictionary has been updated to 'dictionary.txt'.")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except IOError:
        print("IOError: An error occurred while writing to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


main()
