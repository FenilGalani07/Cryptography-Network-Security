from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import base64

# RSA key generation
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Save and load keys as needed, here we're working with them directly.

# Encryption
message = "Hello RSA!"
cipher = PKCS1_OAEP.new(public_key)
ciphertext = cipher.encrypt(message.encode())
print("Encrypted:", base64.b64encode(ciphertext))

# Decryption
cipher = PKCS1_OAEP.new(private_key)
decrypted_message = cipher.decrypt(ciphertext)
print("Decrypted:", decrypted_message.decode())
