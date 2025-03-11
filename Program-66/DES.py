# Simple DES (S-DES) Encryption and Decryption

# Permutation and Substitution tables for S-DES
P10 = [2, 4, 1, 6, 3, 9, 0, 5, 8, 7]  # P10 Permutation for key
P4 = [1, 3, 2, 0]  # P4 Permutation for subkey
IP = [1, 5, 2, 0, 3, 7, 4, 6]  # Initial permutation
IP_inv = [3, 0, 2, 4, 6, 1, 7, 5]  # Inverse of IP

# S-Boxes for the S-DES algorithm
S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 0, 2]]
S1 = [[0, 1, 2, 3], [2, 0, 3, 1], [3, 0, 1, 2], [1, 3, 0, 2]]

# Helper function to perform a permutation on the input
def permute(input, table):
    return [input[i] for i in table]

# Helper function for key scheduling (Key Generation)
def key_generation(key_10bit):
    key_10bit = [int(b) for b in key_10bit]
    # Apply P10 permutation to the 10-bit key
    key_p10 = permute(key_10bit, P10)
    
    # Split into two 5-bit halves
    left, right = key_p10[:5], key_p10[5:]
    
    # Left shifts
    left = left[1:] + left[:1]  # Left shift by 1
    right = right[1:] + right[:1]  # Left shift by 1
    
    # Combine the two halves and apply P4 permutation to generate subkeys
    key_1 = permute(left + right, P4)
    
    # Second left shift by 2 positions
    left = left[2:] + left[:2]
    right = right[2:] + right[:2]
    
    key_2 = permute(left + right, P4)
    
    return key_1, key_2

# Helper function for the Fiestel function used in rounds
def feistel(input, subkey):
    # Split input into two halves
    left, right = input[:4], input[4:]
    
    # Apply the S-Box operation
    s_input = [int(b) for b in right] + [int(b) for b in subkey]
    
    row = 2 * s_input[0] + s_input[3]
    col = 2 * s_input[1] + s_input[2]
    
    s_output = S0[row][col]
    result = [int(b) for b in bin(s_output)[2:].zfill(2)]
    
    return result

# The main encryption function (2-round S-DES)
def encrypt(plaintext, key):
    # Key generation
    key_1, key_2 = key_generation(key)
    
    # Apply initial permutation
    ip = permute(plaintext, IP)
    
    # Split into two halves (4 bits each)
    left, right = ip[:4], ip[4:]
    
    # Round 1
    left, right = feistel(left, key_1), right
    
    # Round 2
    left, right = feistel(left, key_2), right
    
    # Combine and apply inverse permutation
    combined = left + right
    ciphertext = permute(combined, IP_inv)
    
    return ciphertext

# The main decryption function
def decrypt(ciphertext, key):
    key_1, key_2 = key_generation(key)
    
    # Apply initial permutation
    ip = permute(ciphertext, IP)
    
    # Split into two halves (4 bits each)
    left, right = ip[:4], ip[4:]
    
    # Round 1 (inverse order of subkeys)
    left, right = feistel(left, key_2), right
    
    # Round 2 (inverse order of subkeys)
    left, right = feistel(left, key_1), right
    
    # Combine and apply inverse permutation
    combined = left + right
    plaintext = permute(combined, IP_inv)
    
    return plaintext

# Example usage
if __name__ == "__main__":
    # Key (10 bits) and plaintext (8 bits)
    key = "1010000010"  # 10-bit key
    plaintext = [1, 0, 0, 1, 0, 1, 1, 0]  # 8-bit plaintext (in binary)

    # Encrypt
    encrypted_text = encrypt(plaintext, key)
    print(f"Encrypted Text: {encrypted_text}")

    # Decrypt
    decrypted_text = decrypt(encrypted_text, key)
    print(f"Decrypted Text: {decrypted_text}")
