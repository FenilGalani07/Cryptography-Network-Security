import numpy as np

# Helper function to convert text to numbers (A=0, B=1, ..., Z=25)
def text_to_numbers(text):
    return [ord(char) - ord('a') for char in text.lower() if char.isalpha()]

# Helper function to convert numbers to text (0=A, 1=B, ..., 25=Z)
def numbers_to_text(numbers):
    return ''.join(chr(num + ord('a')) for num in numbers)

# Function to check if a matrix is invertible modulo 26
def is_invertible(matrix):
    determinant = int(np.round(np.linalg.det(matrix))) % 26
    return determinant != 0 and gcd(determinant, 26) == 1

# Helper function to compute the greatest common divisor
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to compute the modular inverse of a number mod 26
def mod_inverse(a, m=26):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Function to find the inverse of a matrix mod 26
def matrix_inverse(matrix):
    # Compute the inverse matrix modulo 26 using numpy
    det = int(np.round(np.linalg.det(matrix))) % 26
    inv_det = mod_inverse(det, 26)
    
    if inv_det is None:
        raise ValueError("The matrix is not invertible modulo 26.")
    
    # Calculate the adjugate matrix (mod 26)
    adjugate = np.round(np.linalg.inv(matrix) * np.linalg.det(matrix)).astype(int) % 26
    inverse_matrix = (inv_det * adjugate) % 26
    return inverse_matrix

# Hill cipher encryption function
def encrypt(plaintext, key_matrix):
    # Prepare the text by converting it to numbers
    plaintext_numbers = text_to_numbers(plaintext)
    
    # Pad plaintext to fit the matrix block size
    if len(plaintext_numbers) % key_matrix.shape[0] != 0:
        plaintext_numbers.append(0)  # Padding with 'A' if needed
    
    # Divide the plaintext into blocks and encrypt
    ciphertext_numbers = []
    for i in range(0, len(plaintext_numbers), key_matrix.shape[0]):
        block = np.array(plaintext_numbers[i:i + key_matrix.shape[0]]).reshape(-1, 1)
        encrypted_block = np.dot(key_matrix, block) % 26
        ciphertext_numbers.extend(encrypted_block.flatten())
    
    # Convert the ciphertext numbers back to text
    return numbers_to_text(ciphertext_numbers)

# Hill cipher decryption function
def decrypt(ciphertext, key_matrix):
    # Find the inverse key matrix modulo 26
    inverse_key_matrix = matrix_inverse(key_matrix)
    
    # Prepare the ciphertext by converting it to numbers
    ciphertext_numbers = text_to_numbers(ciphertext)
    
    # Decrypt the ciphertext
    plaintext_numbers = []
    for i in range(0, len(ciphertext_numbers), key_matrix.shape[0]):
        block = np.array(ciphertext_numbers[i:i + key_matrix.shape[0]]).reshape(-1, 1)
        decrypted_block = np.dot(inverse_key_matrix, block) % 26
        plaintext_numbers.extend(decrypted_block.flatten())
    
    # Convert the plaintext numbers back to text
    return numbers_to_text(plaintext_numbers)

# Example usage
if __name__ == "__main__":
    # Define the key matrix for encryption (2x2 matrix)
    key_matrix = np.array([[6, 24], [1, 16]])
    
    # Check if the key matrix is invertible
    if not is_invertible(key_matrix):
        print("The key matrix is not invertible, please choose a different key.")
    else:
        # Example plaintext
        plaintext = "HELLO"
        print("Original Plaintext:", plaintext)
        
        # Encrypt the message
        ciphertext = encrypt(plaintext, key_matrix)
        print("Encrypted Ciphertext:", ciphertext)
        
        # Decrypt the message
        decrypted_text = decrypt(ciphertext, key_matrix)
        print("Decrypted Text:", decrypted_text)
