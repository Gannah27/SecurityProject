from Crypto.PublicKey import RSA, ECC
from Crypto.Cipher import DES, AES
from Crypto.Util import number
from Crypto import Random
from Crypto.PublicKey import ElGamal
import pickle
import os
from RSA import generateprimes,generatepublicKey,coprime

# RSA Key Generation
def generate_rsa_keys():
    Prime_1, Prime_2,publickey=generatepublicKey()
    q,e= coprime(Prime_1,Prime_2)
    privatekey=number.inverse(e,q)
    return privatekey,publickey, q, e, Prime_1, Prime_2

# ECC Key Generation
def generate_ecc_key():
    key = ElGamal.generate(256,None)
    public_key = key.publickey()
    private_key = key.has_private()
    return key, public_key, private_key

# DES Key Generation
def generate_des_key():
    # DES key must be exactly 8 bytes long.
    return Random.get_random_bytes(8)

# AES Key Generation
def generate_aes_key():
    # AES key must be either 16, 24, or 32 bytes long.
    return Random.get_random_bytes(16)

# Key Storage
def store_keys(keys, filename):
    # Convert ECC keys to components for pickling
    # if "ECC" in keys:
    #     ecc_key = keys["ECC"]["key"]
    #     ecc_key_public = keys["ECC"]["public"]
    #     ecc_key_private = keys["ECC"]["private"]
    #     keys["ECC"] = {
    #         "key": (ecc_key.p, ecc_key.g, ecc_key.y),
    #         "public": (ecc_key_public.p, ecc_key_public.g, ecc_key_public.y),
    #         "private": ecc_key_private
    #     }
    with open(filename, 'wb') as f:
        pickle.dump(keys, f)

# Key Distribution
def distribute_keys(filename):
    if not os.path.exists(filename):
        print(f"No such file: {filename}")
        return None

    with open(filename, 'rb') as f:
        keys = pickle.load(f)

    return keys

# Test the key generation functions
def test():
    des_key = generate_des_key()
    aes_key = generate_aes_key()
    ecc_key, ecc_key_public, ecc_key_private = generate_ecc_key()
    rsa_privatekey, rsa_publickey, q, e, Prime_1, Prime_2 = generate_rsa_keys()
    
    print("Generating Keys:")
    print(f"RSA Private Key: {rsa_privatekey}")
    print(f"RSA Public Key: {rsa_publickey}")

    print(f"ECC Key: {ecc_key}")
    print(f"ECC Private Key: {ecc_key_private}")
    print(f"ECC Public Key: {ecc_key_public}")

    des_key = generate_des_key()
    print(f"DES Key: {des_key}")

    aes_key = generate_aes_key()
    print(f"AES Key: {aes_key}")

    # Test key storage and distribution

    keys = {
        "RSA": {
            "private": rsa_privatekey,
            "public": rsa_publickey,
            "q": q,
            "e": e,
            "Prime_1": Prime_1,
            "Prime_2": Prime_2
        },
        "ECC": {
            "key": ecc_key,
            "private": ecc_key_private,
            "public": ecc_key_public
        },
        "DES": des_key,
        "AES": aes_key
    }
    
    # Store keys
    store_keys(keys, 'keys.pkl')

    # Distribute keys
    distributed_keys = distribute_keys('keys.pkl')
    print(distributed_keys)

if __name__ == "__main__":
    test()