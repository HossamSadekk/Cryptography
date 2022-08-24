def checkIfAllowed(key):
    if (key in notAllowed):
        print("Invalid key please enter another key :")
        a = input()
        return checkIfAllowed(a)
    else:
        return key


def affineEncryption(plainText, a, b):
    encrypted = ""
    for i in range(0, len(plainText)):
        if (plainText[i] == " "):
            encrypted += " "
        else:
            c = (int(a) * alphabet.index(plainText[i].upper()) + int(b)) % 26
            encrypted += alphabet[c]
    return encrypted


def affineDecryption(cipher, a, b):
    decrypted = ""
    for i in range(0, len(cipher)):
        if (cipher[i] == " "):
            decrypted += " "
        else:
            c = pow(int(a), -1, 26) * (alphabet.index(cipher[i].upper()) - int(b)) % 26
            decrypted += alphabet[c].lower()
    return decrypted


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
notAllowed = ["2", "4", "6", "8", "10", "12", "13", "14", "16", "18", "20", "22", "24"]
plainText = input("enter the plain text: ")
a = checkIfAllowed(input("enter 'a' key: "))
b = input("enter 'b' key: ")
encrypted = affineEncryption(plainText, a, b)
print("the encrypted plain text: ", encrypted)
print("the decrypted cipher text: ", affineDecryption(encrypted, a, b))
