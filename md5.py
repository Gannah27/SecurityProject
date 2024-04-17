from hashlib import sha256

input_ = input('Enter something to be hashed: ')
print(sha256(input_.encode('utf-8')).hexdigest())