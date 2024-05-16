from key_management_module import *
import socket
import threading
import pickle
import sys

class Client:
    def __init__(self):
        (clientsock, (ip, port)) = server_socket.accept()
        self.clientT = ClientThread(ip, port, clientsock)
        self.clientT.start()

class ClientThread(threading.Thread):
    def __init__(self,ip,port,clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.csocket = clientsocket
        print("[+] New thread started for ",ip,":",str(port))

    def run(self):
        print("Connection from : ",self.ip,":",str(self.port))

        ecc_key, ecc_key_public, ecc_key_private = generate_ecc_key()
        rsa_privatekey, rsa_publickey, q, e, Prime_1, Prime_2 = generate_rsa_keys()

        keys = {
            "RSA": {
                "private": rsa_privatekey,
                "public": rsa_publickey,
                "q": q,
                "e": e,
                "Prime_1": Prime_1,
                "Prime_2": Prime_2
            },
            "ECC": {
                "key": ecc_key,
                "private": ecc_key_private,
                "public": ecc_key_public
            },
            "DES": des_key,
            "AES": aes_key
        }

        ecc_key = keys["ECC"]["key"]
        ecc_key_public = keys["ECC"]["public"]
        ecc_key_private = keys["ECC"]["private"]
        keys["ECC"] = {
            "key": (ecc_key.p, ecc_key.g, ecc_key.y),
            "public": (ecc_key_public.p, ecc_key_public.g, ecc_key_public.y),
            "private": ecc_key_private
        }
        
        # Pickle the content
        data = pickle.dumps(keys)
        
        # Send the pickled content
        self.csocket.send(data)
        self.csocket.send("".encode('utf-8'))
        self.csocket.close()
        
        
        

host = "0.0.0.0"
port = 12345
# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))

des_key = generate_des_key()
aes_key = generate_aes_key()

while True:
    server_socket.listen(4)
    print("Listening for incoming connections...")
    newClient = Client()

