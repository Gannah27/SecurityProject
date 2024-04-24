import threading
import queue
from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes

class EncryptionWorker(threading.Thread):
    def __init__(self, type, plaintext_queue, ciphertext_queue):
        threading.Thread.__init__(self)
        self.plaintext_queue = plaintext_queue
        self.ciphertext_queue = ciphertext_queue
        self.type = type

        # self.cipher = DES.new(self.key, DES.MODE_EAX) for DES encryption
        if self.type == "DES":
            self.key = get_random_bytes(8) # DES key must be 8 bytes long
            self.cipher = DES.new(self.key, DES.MODE_EAX) # DES.MODE_EAX is a block cipher mode that provides authenticated encryption
        
        elif self.type == "AES":
            self.key = get_random_bytes(16) # AES key must be either 16, 24, or 32 bytes long
            self.cipher = AES.new(self.key, AES.MODE_EAX) # AES.MODE_EAX is a block cipher mode that provides authenticated encryption
    def run(self):
        while True:
            plaintext = self.plaintext_queue.get() # get the plaintext from the plaintext queue
            if plaintext is None:
                break
            ciphertext, tag = self.cipher.encrypt_and_digest(plaintext.encode("utf8"))
            self.ciphertext_queue.put((ciphertext, tag))


plaintext_queue = queue.Queue()
ciphertext_queue = queue.Queue()

plaintext_queue.put("Hi there!")
print("queue size: ", plaintext_queue.qsize())
worker = EncryptionWorker("DES",plaintext_queue, ciphertext_queue)
print("worker started")
worker.start()
x = ciphertext_queue.get()
ciphertext, tag = x

print(type(ciphertext))

# Decrypt ciphertext
if worker.type == "DES":
    cipher = DES.new(worker.key, DES.MODE_EAX, nonce=worker.cipher.nonce)
elif worker.type == "AES":
    cipher = AES.new(worker.key, AES.MODE_EAX, nonce=worker.cipher.nonce)
decrypted_plaintext = cipher.decrypt_and_verify(ciphertext, tag)

# Print decrypted plaintext
print("Decrypted:", decrypted_plaintext.decode("utf8"))
