import hashlib

# Function to generate SHA-1 hash of a string
def generate_sha1_hash(input_string):
    # Create a new sha1 hash object
    sha1_hash = hashlib.sha1()
    
    # Update the object with the input string (encoded to bytes)
    sha1_hash.update(input_string.encode('utf-8'))
    
    # Return the hexadecimal representation of the SHA-1 hash
    return sha1_hash.hexdigest()

# Example usage
if __name__ == "__main__":
    input_string = "Hello, SHA-1!"
    
    # Generate the SHA-1 hash
    sha1_hash = generate_sha1_hash(input_string)
    
    print(f"Input String: {input_string}")
    print(f"SHA-1 Hash: {sha1_hash}")
