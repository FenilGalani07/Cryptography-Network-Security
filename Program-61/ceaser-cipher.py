def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
           
            offset = 65 if char.isupper() else 97
            
            shifted = (ord(char) - offset + shift) % 26 + offset
            ciphertext += chr(shifted)
        else:
            ciphertext += char  
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
           
            offset = 65 if char.isupper() else 97
          
            shifted = (ord(char) - offset - shift) % 26 + offset
            plaintext += chr(shifted)
        else:
            plaintext += char  
    return plaintext


shift = 3
plaintext = "Hello, World!"
ciphertext = caesar_encrypt(plaintext, shift)
decrypted_text = caesar_decrypt(ciphertext, shift)

print("Original Text:", plaintext)
print("Encrypted Text:", ciphertext)
print("Decrypted Text:", decrypted_text)
