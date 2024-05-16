import threading
import queue
from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes


class EncryptionWorker():
    def __init__(self, type, plaintext_queue, ciphertext_queue, key):
        self.plaintext_queue = plaintext_queue
        self.ciphertext_queue = ciphertext_queue
        self.type = type
        self.key = key

        if self.type == "DES":
            self.cipher = DES.new(self.key, DES.MODE_CFB)
            self.iv = self.cipher.iv

        elif self.type == "AES":
            self.cipher = AES.new(self.key, AES.MODE_CFB)
            self.iv = self.cipher.iv

    def encrypt(self):
        while True:
            if self.plaintext_queue.empty():
                break
            plaintext = self.plaintext_queue.get()
            if plaintext is None:
                break
            ciphertext = self.cipher.encrypt(plaintext.encode("utf8"))
            print("Ciphertext before enqueue:", ciphertext)
            self.ciphertext_queue.put((ciphertext, self.iv))


class DecryptionWorker():
    def __init__(self, type, ciphertext_queue, decrypted_queue, key):
        self.ciphertext_queue = ciphertext_queue
        self.decrypted_queue = decrypted_queue
        self.type = type
        self.key = key

    def decrypt(self):
        while True:
            if self.ciphertext_queue.empty():
                break
            ciphertext = self.ciphertext_queue.get()
            if ciphertext is None:
                break
            ciphertext, iv = ciphertext
            print("Ciphertext after dequeue:", ciphertext)
            if self.type == "DES":
                self.cipher = DES.new(self.key, DES.MODE_CFB, iv=iv)

            elif self.type == "AES":
                self.cipher = AES.new(self.key, AES.MODE_CFB, iv=iv)

            decrypted_plaintext = self.cipher.decrypt(ciphertext)
            self.decrypted_queue.put(decrypted_plaintext)

# '''
# def main():
#     print("Starting...")
#     plaintext_queue = queue.Queue()
#     ciphertext_queue = queue.Queue()

#     plaintext_queue.put("Hi there!")
#     plaintext_queue.put(None)  # Signal the end of the queue
#     key = get_random_bytes(16)
#     worker = EncryptionWorker("AES", plaintext_queue, ciphertext_queue, key)
#     worker.start()

#     worker.join()  # Wait for the worker to finish

#     if ciphertext_queue.empty():
#         print("Ciphertext_queue is empty")
#     else:
#         print("Ciphertext_queue is not empty")

#     decrypted_queue = queue.Queue()
#     print("Decrypting...")
#     worker_decrypt = DecryptionWorker("AES", ciphertext_queue, decrypted_queue, key)
#     worker_decrypt.start()

#     worker_decrypt.join()  # Wait for the worker to finish

#     decrypted_plaintext = decrypted_queue.get()
#     print("Decrypted:", decrypted_plaintext)


# if __name__ == "__main__":
#     main()
# '''