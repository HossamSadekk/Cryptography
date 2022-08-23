def encryption(plainText, key):
    encrypted = ''

    for i in range(0, len(plainText)):
        if plainText[i] == " ":
            encrypted += " "
        else:
            c = (alphabet.index(plainText[i].upper()) + key) % 26
            encrypted += alphabet[c]

    return encrypted


def decryption(cipherText, key):
    decrypted = ''
    for i in range(0, len(cipherText)):
        if cipherText[i] == " ":
            decrypted += " "
        else:
            c = (alphabet.index(cipherText[i].upper()) - key) % 26
            decrypted += alphabet[c].lower()

    return decrypted


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plainText = input("Enter your plain text: ")
key = input("Enter your key: ")
print('the encrypted plain text is : ', encryption(plainText, key))
print('the decrypted plain text is : ', decryption(encryption(plainText, key)))
