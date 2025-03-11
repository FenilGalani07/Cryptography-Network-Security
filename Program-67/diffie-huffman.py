# Function to perform modular exponentiation (g^a mod p)
def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

# Diffie-Hellman Key Exchange function
def diffie_hellman(p, g, private_key_1, private_key_2):
    # Party 1 calculates their public key (A = g^a mod p)
    A = mod_exp(g, private_key_1, p)
    
    # Party 2 calculates their public key (B = g^b mod p)
    B = mod_exp(g, private_key_2, p)
    
    print(f"Party 1 public key: {A}")
    print(f"Party 2 public key: {B}")
    
    # Party 1 calculates the shared secret key using Party 2's public key (K1 = B^a mod p)
    shared_secret_1 = mod_exp(B, private_key_1, p)
    
    # Party 2 calculates the shared secret key using Party 1's public key (K2 = A^b mod p)
    shared_secret_2 = mod_exp(A, private_key_2, p)
    
    print(f"Party 1 computed shared secret key: {shared_secret_1}")
    print(f"Party 2 computed shared secret key: {shared_secret_2}")
    
    # Both parties should have the same shared secret key
    if shared_secret_1 == shared_secret_2:
        return shared_secret_1
    else:
        raise ValueError("Key exchange failed: Secret keys do not match.")

# Example usage
if __name__ == "__main__":
    # Public parameters
    p = 23  # A prime number (public)
    g = 5   # A primitive root modulo p (public)
    
    # Private keys (these would be secret in a real-world scenario)
    private_key_1 = 6  # Party 1's private key
    private_key_2 = 15  # Party 2's private key
    
    # Perform Diffie-Hellman Key Exchange
    shared_secret = diffie_hellman(p, g, private_key_1, private_key_2)
    print(f"Shared secret key: {shared_secret}")
