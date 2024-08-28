#Layyana Junaid BSAI-3A

def find_maximum(*numbers):
    max_value = numbers[0]

    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

print(find_maximum(3, 5, 7, 2, 8))
print(find_maximum(-1, -5, -3))
