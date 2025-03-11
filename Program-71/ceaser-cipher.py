def caesar_cipher_encrypt(plaintext, shift):
    encrypted = ""
    for char in plaintext:
        if char.isalpha():
            shifted = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
            encrypted += shifted.upper() if char.isupper() else shifted
        else:
            encrypted += char
    return encrypted

def caesar_cipher_decrypt(ciphertext, shift):
    return caesar_cipher_encrypt(ciphertext, -shift)

# Example Usage
message = "Hello, World!"
shift = 3
encrypted_message = caesar_cipher_encrypt(message, shift)
decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)

print("Encrypted:", encrypted_message)
print("Decrypted:", decrypted_message)
