from Crypto.Hash import SHA256
from Crypto.Hash import MD5

# input_ = input('Enter something to be hashed: ')
# input_ = input('Enter something to be hashed: ')

# hash_object = MD5.new()
# hash_object.update(input_.encode('utf-8'))

# print("The byte equivalent of hash is : ", end ="")
# print(hash_object.digest())

# input_ = input('Enter something to be hashed: ')
# hash_object = SHA256.new()
# hash_object.update(input_.encode('utf-8'))

# print("The hexadecimal representation of the hash is:", hash_object.hexdigest())
def hash_string(x):
    hash_object = SHA256.new()
    hash_object.update(x.encode('utf-8'))
    return hash_object.hexdigest()

def compare_hashes(hash1, hash2):
    return hash1 == hash2