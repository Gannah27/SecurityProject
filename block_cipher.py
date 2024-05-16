import queue
from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes


def create_cipher(type, key, iv=None):
    if type == "DES":
        return DES.new(key, DES.MODE_CFB, iv=iv)
    elif type == "AES":
        return AES.new(key, AES.MODE_CFB, iv=iv)

def encrypt_message(type, plaintext, key, iv=None):
    cipher = create_cipher(type, key, iv)
    iv = cipher.iv
    ciphertext = cipher.encrypt(plaintext.encode("utf8"))
    return ciphertext, iv

def decrypt_message(type, key, iv, ciphertext):
    # Create a new cipher for decryption
    cipher = create_cipher(type, key, iv)
    decrypted_plaintext = cipher.decrypt(ciphertext)
    return decrypted_plaintext