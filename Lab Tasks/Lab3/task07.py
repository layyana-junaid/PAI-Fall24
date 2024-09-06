#Layyana Junaid 23k-0056 BSAI-3A
#Lab 3 task 7

def identify_and_replace(file_path):
    try:
        with open(file_path, "r") as file:
            document = file.read()

        print("Original content:", document)

        corrected_document = document.replace("t", "p")

        print("Corrected content:", corrected_document)

        with open(file_path, "w") as file:
            file.write(corrected_document)

    except FileNotFoundError:
        print("Error: The file does not exist.")

def main():
    identify_and_replace("replacement.txt")

main()
