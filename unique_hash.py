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

# Create a list of the hashes
hashes = [hash_md5, hash_sha1, hash_sha224, hash_sha256, hash_sha384, hash_sha512]

# Iterate over the pairs of hashes
for i in range(len(hashes)):
    for j in range(i+1, len(hashes)):
        # Calculate the difference between the two hashes
        diff = int(hashes[i], 16) ^ int(hashes[j], 16)
        # Convert the difference to a binary string
        diff_bin = bin(diff)[2:]
        # Count the number of 1s in the binary string
        num_ones = diff_bin.count('1')
        # Print the difference between the two hashes
        print(f"{hashes[i]:<64s} {hashes[j]:<64s} {num_ones} bits differ")
        print("-" * 150)
