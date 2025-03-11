import random
from sympy import isprime

# Function to calculate the greatest common divisor (gcd)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to compute modular multiplicative inverse
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Function to generate RSA keys
def generate_rsa_keys(bits=8):
    # Step 1: Choose two distinct primes p and q
    p = generate_prime(bits)
    q = generate_prime(bits)
    
    # Ensure p != q
    while p == q:
        q = generate_prime(bits)
    
    # Step 2: Compute n = p * q
    n = p * q
    
    # Step 3: Compute Euler's Totient function: φ(n) = (p-1)*(q-1)
    phi_n = (p - 1) * (q - 1)
    
    # Step 4: Choose public exponent e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
    e = random.randint(2, phi_n - 1)
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)
    
    # Step 5: Compute private exponent d such that (d * e) % φ(n) = 1
    d = mod_inverse(e, phi_n)
    
    # Public key (n, e) and Private key (n, d)
    public_key = (n, e)
    private_key = (n, d)
    
    return public_key, private_key

# Function to generate a prime number of a given bit length
def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if isprime(num):
            return num

# RSA encryption function
def rsa_encrypt(message, public_key):
    n, e = public_key
    # Convert the message to an integer
    message_int = int.from_bytes(message.encode(), 'big')
    # Encrypt the message: c = m^e mod n
    cipher = pow(message_int, e, n)
    return cipher

# RSA decryption function
def rsa_decrypt(ciphertext, private_key):
    n, d = private_key
    # Decrypt the message: m = c^d mod n
    decrypted_int = pow(ciphertext, d, n)
    # Convert the decrypted integer back to a string
    decrypted_message = decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, 'big').decode()
    return decrypted_message

# Example usage
if __name__ == "__main__":
    # Step 1: Generate RSA keys
    public_key, private_key = generate_rsa_keys(bits=8)  # Using 8-bit for simplicity, use 2048-bit for real use
    
    print("Public Key:", public_key)
    print("Private Key:", private_key)
    
    # Step 2: Encrypt a message
    message = "Hello RSA!"
    encrypted_message = rsa_encrypt(message, public_key)
    print(f"Encrypted Message (Ciphertext): {encrypted_message}")
    
    # Step 3: Decrypt the message
    decrypted_message = rsa_decrypt(encrypted_message, private_key)
    print(f"Decrypted Message: {decrypted_message}")
