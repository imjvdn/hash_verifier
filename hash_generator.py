import hashlib

# Open the file in binary mode
with open('test.txt', 'rb') as file:
    # Read the contents of the file
    contents = file.read()
    # Calculate the hash using the MD5 algorithm
    hash_md5 = hashlib.md5(contents).hexdigest()
    # Calculate the hash using the SHA-1 algorithm
    hash_sha1 = hashlib.sha1(contents).hexdigest()
    # Calculate the hash using the SHA-224 algorithm
    hash_sha224 = hashlib.sha224(contents).hexdigest()
    # Calculate the hash using the SHA-256 algorithm
    hash_sha256 = hashlib.sha256(contents).hexdigest()
    # Calculate the hash using the SHA-384 algorithm
    hash_sha384 = hashlib.sha384(contents).hexdigest()
    # Calculate the hash using the SHA-512 algorithm
    hash_sha512 = hashlib.sha512(contents).hexdigest()

# Print the calculated hashes
print(f"{'MD5 hash:'} {hash_md5}")
print(f"{'SHA-1 hash:'} {hash_sha1}")
print(f"{'SHA-224 hash:'} {hash_sha224}")
print(f"{'SHA-256 hash:'} {hash_sha256}")
print(f"{'SHA-384 hash:'} {hash_sha384}")
print(f"{'SHA-512 hash:'} {hash_sha512}")
