#Layyana Junaid BSAI-3A
#task 7

def averageTemperature(temperatures):
    average = sum(temperatures) / len(temperatures)
    print(f"Average Temperature: {average:.2f}")

def highestAndlowest(temperatures):
    highestTemperature = temperatures[0]
    lowestTemperature = temperatures[0]

    for temp in temperatures:
        if temp > highestTemperature:
            highestTemperature = temp
        if temp < lowestTemperature:
            lowestTemperature = temp

    print(f"Highest Temperature: {highestTemperature}")
    print(f"Lowest Temperature: {lowestTemperature}")

def sortTemperature(temperatures):
    sortedTemperatures = sorted(temperatures)
    print(f"Temperatures in Ascending Order: {sortedTemperatures}")

def dayToRemove(temperatures, remove):
    if remove is not None:
        if 0 <= remove < len(temperatures):
            removedTemperature = temperatures.pop(remove)
            print(f"Removed Temperature Record for Day {remove + 1}: {removedTemperature}")
        else:
            print("Invalid day index. No record removed.")
    
    print(f"Updated Temperature Records: {temperatures}")

temperatures = [72, 68, 75, 79, 81, 80]
day_to_remove = 5  

averageTemperature(temperatures)
highestAndlowest(temperatures)
sortTemperature(temperatures)
dayToRemove(temperatures, day_to_remove)
