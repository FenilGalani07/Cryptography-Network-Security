def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Check if character is uppercase or lowercase
            offset = 65 if char.isupper() else 97
            # Perform shift and wrap around if necessary
            shifted = (ord(char) - offset + shift) % 26 + offset
            ciphertext += chr(shifted)
        else:
            ciphertext += char  # Non-alphabetic characters remain unchanged
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Check if character is uppercase or lowercase
            offset = 65 if char.isupper() else 97
            # Reverse the shift and wrap around if necessary
            shifted = (ord(char) - offset - shift) % 26 + offset
            plaintext += chr(shifted)
        else:
            plaintext += char  # Non-alphabetic characters remain unchanged
    return plaintext

# Example usage:
shift = 3
plaintext = "Hello, World!"
ciphertext = caesar_encrypt(plaintext, shift)
decrypted_text = caesar_decrypt(ciphertext, shift)

print("Original Text:", plaintext)
print("Encrypted Text:", ciphertext)
print("Decrypted Text:", decrypted_text)
