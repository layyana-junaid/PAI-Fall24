#Layyana Junaid BS AI - 3A
#task 8- creating a currency converter

def DisplayCurrenyinfo():
    print("Welcome to Currency Converter: ")
    print("1- Euro.")
    print("2- Dollar.")
    print("3- PKR.")
    print("4- INR.")
    print("5- Yen")

def ConversionRates(fromCurr, toCurr):
    conversionRates = {
        'Euro': {'Dollar': 1.07, 'PKR': 308.40, 'INR': 92.20, 'Yen': 149.76},
        'Dollar': {'Euro': 0.93, 'PKR': 287.50, 'INR': 86.00, 'Yen': 140.65},
        'PKR': {'Euro': 0.0032, 'Dollar': 0.0035, 'INR': 0.30, 'Yen': 0.49},
        'INR': {'Euro': 0.011, 'Dollar': 0.012, 'PKR': 3.31, 'Yen': 1.63},
        'Yen': {'Euro': 0.0067, 'Dollar': 0.0071, 'PKR': 2.04, 'INR': 0.61}
    }
    return  conversionRates.get(fromCurr, {}).get(toCurr, None)

def main():
    DisplayCurrenyinfo()
    option = input("Enter the input currency: ")

    currencies = ["Euro", "Dollar", "PKR", "INR", "Yen"]
    fromCurr = currencies[int(option) - 1]
    amount = float(input(f"Enter the amount to convert in {fromCurr}: "))

    for i, currency in enumerate(currencies, 1):
        if currency != fromCurr:
            print(f"{i}.{currency}")

    choice = input(f"Choose currency to convert to (1-{len(currencies) - 1}): ")
    toCurr = currencies[int(choice)]

    rate = ConversionRates(fromCurr, toCurr)
    if rate is None:
        print("Conversion rate not available.")
        return

    convertedAmount = amount * rate
    print(f"{amount} {fromCurr} is equals to {convertedAmount: 2f} {toCurr}")

main()