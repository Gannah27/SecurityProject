import hashlib

input_ = input('Enter something to be hashed: ')

input_bytes = input_.encode('utf-8') #string into bytes
result = hashlib.md5(input_bytes)

print("The byte equivalent of hash is : ", end ="")
print(result.digest())
