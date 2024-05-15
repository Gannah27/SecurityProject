from key_management_module import *
import socket
import threading
import pickle
import authentication_module
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

        rsa_private_key, rsa_public_key = generate_rsa_keys()
        ecc_private_key, ecc_public_key = generate_ecc_keys()
        

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

        # Pickle the content
        data = pickle.dumps(keys)
        
        # Send the pickled content
        self.csocket.send(data)
        self.csocket.send("".encode('utf-8'))
        self.csocket.close()
    def receivedata(self):
        while True:
            data = self.csocket.recv(1024).decode()
            # Split the received data into two parameters
            username, password, type = data.split(',')
            response = ""
            if type == "add":
                response = authentication_module.signup(username, password)
                self.csocket.send(response.encode())
                if response:
                    self.run()
            elif type == "verify":
                response = authentication_module.login(username, password)
                self.csocket.send(response.encode())
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
    newClient.clientT.receivedata()
