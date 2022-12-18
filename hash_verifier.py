import hashlib
import sys

def calculate_hash(filename, algorithm):
    # Open the file in binary mode
    with open(filename, 'rb') as file:
        # Read the contents of the file
        contents = file.read()
        # Calculate the hash using the specified algorithm
        if algorithm == 'md5':
            hash = hashlib.md5(contents).hexdigest()
        elif algorithm == 'sha1':
            hash = hashlib.sha1(contents).hexdigest()
        elif algorithm == 'sha224':
            hash = hashlib.sha224(contents).hexdigest()
        elif algorithm == 'sha256':
            hash = hashlib.sha256(contents).hexdigest()
        elif algorithm == 'sha384':
            hash = hashlib.sha384(contents).hexdigest()
        elif algorithm == 'sha512':
            hash = hashlib.sha512(contents).hexdigest()
        elif algorithm == 'sha512_224':
            hash = hashlib.sha3_224(contents).hexdigest()
        elif algorithm == 'sha512_256':
            hash = hashlib.sha3_256(contents).hexdigest()
        else:
            print("Invalid algorithm")
            sys.exit(1)
    return hash

def main():
    # Parse the command line arguments
    if len(sys.argv) != 3:
        print("Usage: python hash_checker.py <hash> <filename>")
        sys.exit(1)
    supplied_hash = sys.argv[1]
    filename = sys.argv[2]

    # Calculate the hash of the file using each of the supported algorithms
    for algorithm in ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'sha512_224', 'sha512_256']:
        calculated_hash = calculate_hash(filename, algorithm)
        # Compare the calculated hash with the supplied hash
        if calculated_hash == supplied_hash:
            print("Name of the file:", filename)
            print("Checksum is valid")
            print("Algorithm used:", algorithm)
            print("Checksum provided:", supplied_hash)
            print("Checksum calculated:", calculated_hash)
            sys.exit(0)
    print("Name of the file:", filename)
    print("Checksum is not valid")

if __name__ == '__main__':
    main()
