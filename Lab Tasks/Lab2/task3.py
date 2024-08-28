#Layyana Junaid BSAI-3A
#task 3

def ConvrertURL():
    user = input("Enter a URL that starts with 'http://www.( user url )':")
    prefix = "http://www."

    if user.startswith(prefix):
         userURL = user[len(prefix):]

         if userURL:
              newURL = f"{userURL}.com"
              print(f"New URL: {newURL}.")
         else:
               print("The URL part after 'http://www.' is empty.")
    else:
        print(f"The URL should start with '{prefix}'.")

ConvrertURL()