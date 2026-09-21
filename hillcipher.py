import numpy as np
import math

# Key matrix
key = np.array([[3, 3],
                [2, 5]])

MOD = 26


# Find modular inverse
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


# Find inverse of key matrix modulo 26
def inverse_matrix(matrix):
    a, b = matrix[0]
    c, d = matrix[1]

    determinant = (a * d - b * c) % MOD
    det_inverse = mod_inverse(determinant, MOD)

    if det_inverse is None:
        raise ValueError("Key matrix is not invertible.")

    inverse = np.array([[d, -b],
                        [-c, a]])

    inverse = (det_inverse * inverse) % MOD

    return inverse.astype(int)


# Encryption
def encrypt(text):
    text = text.upper().replace(" ", "")

    # Add X if length is odd
    if len(text) % 2 != 0:
        text += "X"

    result = ""

    for i in range(0, len(text), 2):
        p = np.array([
            [ord(text[i]) - ord('A')],
            [ord(text[i + 1]) - ord('A')]
        ])

        c = np.dot(key, p) % MOD

        result += chr(int(c[0][0]) + ord('A'))
        result += chr(int(c[1][0]) + ord('A'))

    return result


# Decryption
def decrypt(ciphertext):
    inverse_key = inverse_matrix(key)

    result = ""

    for i in range(0, len(ciphertext), 2):
        c = np.array([
            [ord(ciphertext[i]) - ord('A')],
            [ord(ciphertext[i + 1]) - ord('A')]
        ])

        p = np.dot(inverse_key, c) % MOD

        result += chr(int(p[0][0]) + ord('A'))
        result += chr(int(p[1][0]) + ord('A'))

    return result


# Main program
plaintext = input("Enter plaintext: ")

encrypted_text = encrypt(plaintext)
print("Encrypted Text:", encrypted_text)

decrypted_text = decrypt(encrypted_text)
print("Decrypted Text:", decrypted_text)