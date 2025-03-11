import hashlib
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


# Function to generate SHA-1 hash of a message
def generate_sha1_hash(message):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(message.encode('utf-8'))
    return sha1_hash.hexdigest()


# Function to sign a message with the private key (RSA-based signature)
def sign_message(message, private_key):
    n, d = private_key
    # Hash the message
    message_hash = generate_sha1_hash(message)
    message_int = int(message_hash, 16)

    # Encrypt the hash with the private key (m^d mod n)
    signature = pow(message_int, d, n)
    return signature


# Function to verify the signature with the public key (RSA-based signature verification)
def verify_signature(message, signature, public_key):
    n, e = public_key
    # Hash the message
    message_hash = generate_sha1_hash(message)
    message_int = int(message_hash, 16)

    # Decrypt the signature with the public key (s^e mod n)
    decrypted_hash = pow(signature, e, n)

    # Verify if the decrypted hash matches the message's hash
    return decrypted_hash == message_int


# Example usage
if __name__ == "__main__":
    # Step 1: Generate RSA keys
    public_key, private_key = generate_rsa_keys(bits=8)  # 8-bit for demonstration, use larger sizes in production
    
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")
    
    # Step 2: Sign a message
    message = "Hello, this is a secret message!"
    signature = sign_message(message, private_key)
    print(f"Signature: {signature}")
    
    # Step 3: Verify the signature
    is_verified = verify_signature(message, signature, public_key)
    print(f"Signature Verified: {is_verified}")
