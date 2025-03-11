from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# AES Encryption
def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return encrypted

# AES Decryption
def aes_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted.decode()

# Example usage
if __name__ == "__main__":
    key = get_random_bytes(16)  # 16-byte key for AES-128
    plaintext = "This is a secret message."
    
    # Encrypt
    ciphertext = aes_encrypt(plaintext, key)
    print(f"Ciphertext: {ciphertext.hex()}")
    
    # Decrypt
    decrypted_text = aes_decrypt(ciphertext, key)
    print(f"Decrypted Text: {decrypted_text}")
