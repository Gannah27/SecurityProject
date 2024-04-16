from Crypto.Util import number
from math import gcd

def generateprimes(n_length):
    while True:
        primeNum1 = number.getPrime(n_length)
        primeNum2 = number.getPrime(n_length)
        if(primeNum1!=primeNum2):
            break
    return primeNum1,primeNum2
def generatepublicKey():
    firstPrime, secondprime = generateprimes(512)
    return firstPrime, secondprime ,firstPrime*secondprime
def coprime(prime1,prime2):
    q=(prime1-1)*(prime2-1)
    candidate_e=1
    for i in range(q,-1,-1):
        if gcd(q,i)==1:
            candidate_e=i
            break
    return q,candidate_e
def encryption(message,e,publickey):
    return pow(message,e,publickey)

def decryption(message,privatekey,publickey):
    return pow(message,privatekey,publickey)
Prime_1, Prime_2,publickey=generatepublicKey()
q,e= coprime(Prime_1,Prime_2)
privatekey=number.inverse(e,q)
print(privatekey)

message= int(input("Enter the message needed "))
option = input("enter 1 for encryption 2 for decryption ")
if option =="1":
    encrypted_message= encryption(message,e,publickey)
    print(encrypted_message)
else:
    decrypted_message= decryption(message,privatekey,publickey)
    print(decrypted_message)