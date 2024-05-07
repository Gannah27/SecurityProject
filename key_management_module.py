from Crypto.PublicKey import RSA, ECC
from Crypto.Cipher import DES, AES
from Crypto import Random
import binascii
import pickle
import os

# RSA Key Generation
def generate_rsa_keys():
    modulus_length = 2048

    key = RSA.generate(modulus_length)
    public_key = key.publickey()

    return key, public_key

# ECC Key Generation
def generate_ecc_keys():
    key = ECC.generate(curve='P-256')
    public_key = key.public_key()

    return key, public_key

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
    rsa_private_key, rsa_public_key = generate_rsa_keys()
    print("Generating Keys:")
    print(f"RSA Private Key: {binascii.hexlify(rsa_private_key.export_key())}")
    print(f"RSA Public Key: {binascii.hexlify(rsa_public_key.export_key())}")

    ecc_private_key, ecc_public_key = generate_ecc_keys()
    print(f"ECC Private Key: {binascii.hexlify(ecc_private_key.export_key(format='DER'))}")
    print(f"ECC Public Key: {binascii.hexlify(ecc_public_key.export_key(format='DER'))}")

    des_key = generate_des_key()
    print(f"DES Key: {binascii.hexlify(des_key)}")

    aes_key = generate_aes_key()
    print(f"AES Key: {binascii.hexlify(aes_key)}")

    # Test key storage and distribution
    # rsa_private_key, rsa_public_key = generate_rsa_keys()
    # ecc_private_key, ecc_public_key = generate_ecc_keys()
    # des_key = generate_des_key()
    # aes_key = generate_aes_key()

    keys = {
        "RSA": {
            "private": rsa_private_key.export_key(),
            "public": rsa_public_key.export_key()
        },
        "ECC": {
            "private": ecc_private_key.export_key(format='DER'),
            "public": ecc_public_key.export_key(format='DER')
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