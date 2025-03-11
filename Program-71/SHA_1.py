import hashlib

# SHA-1 Hash
message = "Hello SHA-1"
sha1_hash = hashlib.sha1(message.encode()).hexdigest()
print("SHA-1 Hash:", sha1_hash)
