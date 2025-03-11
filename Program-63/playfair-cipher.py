import string

# Remove duplicates from the key and create the Playfair matrix
def generate_playfair_matrix(key):
    alphabet = string.ascii_lowercase.replace('j', '')  # Exclude 'j' from the alphabet
    key = ''.join(sorted(set(key), key=key.index))  # Remove duplicate characters from the key
    matrix = key.lower()  # Convert to lowercase

    # Fill the rest of the matrix with remaining characters of the alphabet
    for char in alphabet:
        if char not in matrix:
            matrix += char
    
    # Create the 5x5 matrix (a string)
    return [matrix[i:i+5] for i in range(0, len(matrix), 5)]

# Preprocess the plaintext to handle duplicates and odd length
def preprocess_text(plaintext):
    plaintext = plaintext.lower().replace('j', 'i')  # Treat 'j' as 'i'
    # Split into digraphs, inserting 'x' if necessary
    digraphs = []
    i = 0
    while i < len(plaintext):
        if i + 1 < len(plaintext) and plaintext[i] == plaintext[i+1]:
            digraphs.append(plaintext[i] + 'x')
            i += 1
        elif i + 1 < len(plaintext):
            digraphs.append(plaintext[i] + plaintext[i+1])
            i += 2
        else:
            digraphs.append(plaintext[i] + 'x')
            i += 1
    return digraphs

# Find the position of a letter in the Playfair matrix
def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

# Encrypt the plaintext using the Playfair cipher
def encrypt(plaintext, key):
    matrix = generate_playfair_matrix(key)
    digraphs = preprocess_text(plaintext)
    
    ciphertext = []
    for digraph in digraphs:
        r1, c1 = find_position(matrix, digraph[0])
        r2, c2 = find_position(matrix, digraph[1])
        
        if r1 == r2:
            ciphertext.append(matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5])  # Same row
        elif c1 == c2:
            ciphertext.append(matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2])  # Same column
        else:
            ciphertext.append(matrix[r1][c2] + matrix[r2][c1])  # Rectangle
    return ''.join(ciphertext)

# Decrypt the ciphertext using the Playfair cipher
def decrypt(ciphertext, key):
    matrix = generate_playfair_matrix(key)
    digraphs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    
    plaintext = []
    for digraph in digraphs:
        r1, c1 = find_position(matrix, digraph[0])
        r2, c2 = find_position(matrix, digraph[1])
        
        if r1 == r2:
            plaintext.append(matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5])  # Same row
        elif c1 == c2:
            plaintext.append(matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2])  # Same column
        else:
            plaintext.append(matrix[r1][c2] + matrix[r2][c1])  # Rectangle
    return ''.join(plaintext)

# Example usage
if __name__ == "__main__":
    key = "keyword"  # Playfair keyword
    plaintext = "Hello World"
    print("Original Plaintext:", plaintext)
    
    ciphertext = encrypt(plaintext, key)
    print("Encrypted Ciphertext:", ciphertext)
    
    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted Text:", decrypted_text)
