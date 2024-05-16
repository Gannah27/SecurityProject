from Crypto.PublicKey import RSA, ECC
from Crypto.Cipher import DES, AES
from Crypto import Random
import pickle
import os
import random

# RSA Key Generation
def generate_rsa_keys():
    modulus_length = 2048

    key = RSA.generate(modulus_length)
    public_key = key.publickey()

    return key, public_key

# DES Key Generation
def generate_des_key():
    # DES key must be exactly 8 bytes long.
    return Random.get_random_bytes(8)
def generate_des_iv():
    return Random.get_random_bytes(DES.block_size)
# AES Key Generation
def generate_aes_key():
    # AES key must be either 16, 24, or 32 bytes long.
    return Random.get_random_bytes(16)
def generate_aes_iv():
    return Random.get_random_bytes(AES.block_size)

# Key Storage
def store_keys(keys, filename):
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
    rsa_privatekey, rsa_publickey = generate_rsa_keys()
    
    print("Generating Keys:")
    print(f"RSA Private Key: {rsa_privatekey}")
    print(f"RSA Public Key: {rsa_publickey}")

    des_key = generate_des_key()
    print(f"DES Key: {des_key}")

    aes_key = generate_aes_key()
    print(f"AES Key: {aes_key}")

    # Test key storage and distribution

    keys = {
        "RSA": {
            "private": rsa_privatekey.export_key(),
            "public": rsa_publickey.export_key()
        },
        "DES": des_key,
        "AES": aes_key
    }
    
    # Store keys
    store_keys(keys, 'keys.txt')

    # Distribute keys
    distributed_keys = distribute_keys('keys.txt')
    print(distributed_keys)

if __name__ == "__main__":
    test()