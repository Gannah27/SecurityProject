
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP



# RSA Encryption
def rsa_encrypt(message, public_key):
    rsa_public_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(rsa_public_key)
    encrypted_message = cipher_rsa.encrypt(message.encode())
    return encrypted_message

# RSA Decryption
def rsa_decrypt(encrypted_message, private_key):
    rsa_private_key = RSA.import_key(private_key)
    cipher_rsa = PKCS1_OAEP.new(rsa_private_key)
    decrypted_message = cipher_rsa.decrypt(encrypted_message).decode()
    return decrypted_message
