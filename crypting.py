
def cryptage(message):
    string = ""
    for char in message:
        string += chr(ord(char) + 12)
    return string
