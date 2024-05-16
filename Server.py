import socket
import threading
import authentication_module
from key_management_module import *
from chatserver import *


class ClientThread(threading.Thread):
    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.csocket = clientsocket
        print(f"[+] New thread started for {ip}:{port}")

    def run(self):
        print(f"Connection from: {self.ip}:{self.port}")
        while True:
            try:
                data = self.csocket.recv(1024).decode()
                if not data:
                    print(f"Connection closed by {self.ip}:{self.port}")
                    break

                print(f"Received data: {data}")

                username, password, req_type = data.split(',')
                if req_type == "add":
                    response = authentication_module.signup(username, password)
                    if response ==0:
                        response = "Sign up successful"

                    else:
                        response = "Invalid request type"
                elif req_type == "verify":
                    response = authentication_module.login(username, password)
                    if response ==0:
                        response = "Log in successful"
                    else:
                        response = "Invalid request type"
                else:
                    response = "Invalid request type"

                print(f"Sending response: {response}")
                self.csocket.send(response.encode())

                if req_type == "add" and response == "Sign up successful":
                    self.send_keys()
                    break
            except Exception as e:
                print(f"Error: {e}")
                break
        self.csocket.close()

    def send_keys(self):
        # ecc_key, ecc_key_public, ecc_key_private = generate_ecc_key()
        rsa_privatekey, rsa_publickey = generate_rsa_keys()

        keys = {
            "RSA": {
                "private": rsa_privatekey.export_key(),
                "public": rsa_publickey.export_key()
            },
            "DES": [des_key, iv_des],
            "AES": [aes_key, iv_aes]
        }


        data = pickle.dumps(keys)
        self.csocket.sendall(data)
        print("Keys sent to client")


def start_server(host='localhost', port=12345):

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))

    global des_key, aes_key, iv_des, iv_aes
    des_key = generate_des_key()
    aes_key = generate_aes_key()
    iv_des = generate_des_iv()
    iv_aes = generate_aes_iv()



    server_socket.listen(4)
    print("Listening for incoming connections...")

    # Start the chat server on a separate thread
    chat_server_thread = threading.Thread(target=start_chat_server)
    chat_server_thread.start()

    while True:
        clientsocket, (ip, port) = server_socket.accept()
        new_thread = ClientThread(ip, port, clientsocket)
        new_thread.start()


if __name__ == "__main__":
    start_server()