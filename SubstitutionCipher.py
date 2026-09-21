import string

# Define the substitution key
alphabet = string.ascii_uppercase
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

def encrypt(text):
    result = ""

    for char in text:
        if char.isupper():
            index = alphabet.index(char)
            result += key[index]
        elif char.islower():
            index = alphabet.index(char.upper())
            result += key[index].lower()
        else:
            result += char

    return result


def decrypt(text):
    result = ""

    for char in text:
        if char.isupper():
            index = key.index(char)
            result += alphabet[index]
        elif char.islower():
            index = key.index(char.upper())
            result += alphabet[index].lower()
        else:
            result += char

    return result


# Main program
plaintext = input("Enter plaintext: ")

encrypted_text = encrypt(plaintext)
print("Encrypted Text:", encrypted_text)

decrypted_text = decrypt(encrypted_text)
print("Decrypted Text:", decrypted_text)