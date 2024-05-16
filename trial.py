from block_cipher import *
from key_management_module import *

msg = "Hello World"
key = generate_aes_key()
iv = generate_aes_iv()  # Generate the IV
print("Length of IV:", len(iv))  # Print the length of the IV
if len(iv) != 16:
    raise ValueError("Incorrect IV length (it must be 16 bytes long)")
else:
    print("Correct IV length")
cipher = create_cipher("AES", key)  # Use the generated IV
ciphertext, iv = encrypt_message("AES", key, iv, msg)
if iv == iv:  # Compare with the correct IV
    print("True")
decrypted_plaintext = decrypt_message("AES", key, iv, ciphertext)
print(decrypted_plaintext)