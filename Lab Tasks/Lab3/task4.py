#Layyana Junaid BSAi - 3A
#Lab 3 task 4

def SaveEmployeeData(filePath, name, cnic, age, salary):
    try:
        with open("employeedata.txt", "w") as file:
          file.write(f"Name: {name}\n")
          file.write(f"CNIC: {cnic}\n")
          file.write(f"Age: {age}\n")
          file.write(f"Salary: {salary}\n")

    except IOError:
        print("IOError: An error occurred while writing to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def appendContactNnumber(filePath, contactNumber):
    try:
        with open(filePath, 'a') as file:
            file.write(f"Contact Number: {contactNumber}\n")
    except IOError:
        print("IOError: An error occurred while appending to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def readFile(filePath):
    try:
        with open(filePath, 'r') as file:
            content = file.read()
            print("\nFile Content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filePath}' was not found.")
    except IOError:
        print("IOError: An error occurred while reading the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    filePath = 'employeedata.txt'
    
    try:
        name = input("Enter employee name: ")
        cnic = input("Enter CNIC number: ")
        age = input("Enter age: ")
        salary = input("Enter salary: ")

        SaveEmployeeData(filePath, name, cnic, age, salary)
        
        contactNumber = input("Enter contact number: ")

        appendContactNnumber(filePath, contactNumber)

        readFile(filePath)
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

main()


