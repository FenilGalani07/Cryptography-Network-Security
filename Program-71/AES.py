from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# AES Encryption
key = get_random_bytes(16)  # AES key of 128 bits
cipher = AES.new(key, AES.MODE_CBC)
plaintext = b'Hello AES!'
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
print("Encrypted:", ciphertext)

# AES Decryption
decipher = AES.new(key, AES.MODE_CBC, cipher.iv)
decrypted_message = unpad(decipher.decrypt(ciphertext), AES.block_size)
print("Decrypted:", decrypted_message.decode())
