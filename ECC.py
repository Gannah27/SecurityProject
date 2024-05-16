from Crypto.PublicKey import ElGamal
import common
def to_long(plaintext):
    for i in plaintext:
        lnumber
    return lnumber

def generate_ecc_key():
    key = ElGamal.generate(256,None)
    public_key = key.publickey()
    private_key = key.has_private()
    return key, public_key, private_key

# Encrypt using public key
def encrypt_message(message, key):
    print(public_key.y)

    ciphertext = key._encrypt(message.encode(),public_key.y)
    return ciphertext

# Decrypt using private key
def decrypt_message(ciphertext):

    plaintext = key._decrypt(ciphertext)
    return plaintext

# Generate ECC key pair
# key = ElGamal.generate(256,None)
# print(key)
# # Get public key
# public_key = key.publickey()
# print(public_key)
# # Get private key
# private_key = key.has_private()
# print(private_key)


# Example usage
# key = generate_key()
# public_key = key.publickey()
# private_key = key.has_private()

# message = "helloworld"
# print("Original Message:", message)
# message=common.text_to_numbers(message)
# print(message.encode("utf8"))
# ciphertext = encrypt_message(message, public_key)
# print(decrypt_message(ciphertext))
# plaintext = common.numbers_to_text(decrypt_message(ciphertext))
# print("Encrypted Message:", ciphertext)
# print("Decrypted Message:", plaintext)
