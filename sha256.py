from Crypto.Hash import SHA256

input_ = input('Enter something to be hashed: ')
hash_object = SHA256.new()
hash_object.update(input_.encode('utf-8'))

print("The hexadecimal representation of the hash is:", hash_object.hexdigest())
