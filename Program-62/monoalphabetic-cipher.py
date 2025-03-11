import string
import random


def generate_key():
    alphabet = string.ascii_lowercase
    shuffled = list(alphabet)
    random.shuffle(shuffled)
    key = dict(zip(alphabet, shuffled))
    return key


def encrypt(plaintext, key):
    alphabet = string.ascii_lowercase
    plaintext = plaintext.lower()
    ciphertext = []

    for char in plaintext:
        if char in alphabet:
            ciphertext.append(key[char])
        else:
            ciphertext.append(char)  
    
    return ''.join(ciphertext)


def decrypt(ciphertext, key):
   
    inverse_key = {v: k for k, v in key.items()}
    alphabet = string.ascii_lowercase
    ciphertext = ciphertext.lower()
    plaintext = []

    for char in ciphertext:
        if char in alphabet:
            plaintext.append(inverse_key[char])
        else:
            plaintext.append(char) 
    
    return ''.join(plaintext)

if __name__ == "__main__":

    key = generate_key()
    
  
    plaintext = "Hello, World!"
    print("Original Plaintext:", plaintext)
    

    ciphertext = encrypt(plaintext, key)
    print("Encrypted Ciphertext:", ciphertext)
    

    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted Text:", decrypted_text)
