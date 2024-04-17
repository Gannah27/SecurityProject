from Crypto.Hash import MD5

input_ = input('Enter something to be hashed: ')

hash_object = MD5.new()
hash_object.update(input_.encode('utf-8'))

print("The byte equivalent of hash is : ", end ="")
print(hash_object.digest())

