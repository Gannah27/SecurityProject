from key_management_module import *
import pickle
from Crypto.PublicKey import ECC
from Crypto.Util import asn1

keys = distribute_keys('client_keys.txt')

# Unpickle the data

for key in keys:
    if key == "RSA":
        print(f"Private Key: {keys[key]['private'].decode('utf-8')}")  # Print the private key
        print(f"Public Key: {keys[key]['public'].decode('utf-8')}")  # Print the public key
    elif key == "ECC":
        # Decode the private key
        ecc_private_key = ECC.import_key(keys[key]['private'])

        # Decode the public key
        ecc_public_key = ECC.import_key(keys[key]['public'])

        # Print the decoded private and public keys
        print("Decoded ECC Private Key:")
        print(ecc_private_key)

        print("Decoded ECC Public Key:")
        print(ecc_public_key)
    else:
        print(f"{key} Key: {keys[key]}")