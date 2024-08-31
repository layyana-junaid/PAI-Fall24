#Layyana Junaid 23k-0056 BSAI-3A
#task 10

def build_message(**info):
    message = []

    for key, value in info.items():
        message.append(f"{key.capitalize()}: {value}")

    messages = '\n'.join(message)

    return messages

info = {
    'name' : 'Layyana',
    'city' : 'Karachi',
    'age' : 20,
}

message2 = build_message(**info)
print(message2)