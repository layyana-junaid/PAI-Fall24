#Layyana Junaid 23k-0056 BSAi-3A
#task 12

def generatingDictionary(keys, values):
    results = {}

    for key, value in zip(keys, values):
        results[key] = value

    return results

def main():
    inputforKeys = input("Enter elements for the first list(comma separated): ")
    keys = inputforKeys.split(",")

    inputforValues = input("Enter the elements for the second list(comma separated): ")
    values = inputforValues.split(",")

    if len(keys) != len(values):
        print("THE LISTS ARE NOT OF THE SAME SIZE!")
        return

    resultantDict = generatingDictionary(keys, values)

    print("Resultant Dictionary: ")
    print(resultantDict)


main()