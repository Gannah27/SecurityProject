from key_management_module import *
import pickle

keys = distribute_keys('client_keys.txt')

# Unpickle the data

for key in keys:
    if key == "RSA":
        print(f"Private Key: {keys[key]['private']}")  # Print the private key
        print(f"Public Key: {keys[key]['public']}")  # Print the public key
    elif key == "ECC":
        # Decode the private key
        ecc_private_key = keys[key]['private']

        # Decode the public key
        ecc_public_key = keys[key]['public']
        ecc_key = keys[key]['key']

        # Print the decoded private and public keys
        print("Decoded ECC Private Key:")
        print(ecc_private_key)

        print("Decoded ECC Public Key:")
        print(ecc_public_key)
    else:
        print(f"{key} Key: {keys[key]}")