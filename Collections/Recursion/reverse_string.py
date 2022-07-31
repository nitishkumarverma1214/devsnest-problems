def reverse_string(string):
    if not string:
        return
    reverse_string(string[1:])
    print(string[0])


string = "Nitish"
reverse_string(string)