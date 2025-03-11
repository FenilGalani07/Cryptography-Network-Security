import string

# Function to generate the key of equal length to the plaintext
def generate_key(plaintext, key):
    key = key.lower()
    key = (key * (len(plaintext) // len(key))) + key[:len(plaintext) % len(key)]
    return key

# Encrypt the plaintext using the Vigenère cipher
def encrypt(plaintext, key):
    alphabet = string.ascii_lowercase
    plaintext = plaintext.lower()
    key = generate_key(plaintext, key)
    
    ciphertext = []
    
    for p, k in zip(plaintext, key):
        if p in alphabet:  # Encrypt only alphabetic characters
            shift = alphabet.index(k)
            p_idx = alphabet.index(p)
            encrypted_char = alphabet[(p_idx + shift) % 26]
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(p)  # Non-alphabetic characters are not encrypted
            
    return ''.join(ciphertext)

# Decrypt the ciphertext using the Vigenère cipher
def decrypt(ciphertext, key):
    alphabet = string.ascii_lowercase
    ciphertext = ciphertext.lower()
    key = generate_key(ciphertext, key)
    
    plaintext = []
    
    for c, k in zip(ciphertext, key):
        if c in alphabet:  # Decrypt only alphabetic characters
            shift = alphabet.index(k)
            c_idx = alphabet.index(c)
            decrypted_char = alphabet[(c_idx - shift) % 26]
            plaintext.append(decrypted_char)
        else:
            plaintext.append(c)  # Non-alphabetic characters are not decrypted
    
    return ''.join(plaintext)

# Example usage
if __name__ == "__main__":
    key = "KEYWORD"  # Vigenère cipher key
    plaintext = "Hello World!"
    
    print("Original Plaintext:", plaintext)
    
    ciphertext = encrypt(plaintext, key)
    print("Encrypted Ciphertext:", ciphertext)
    
    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted Text:", decrypted_text)
