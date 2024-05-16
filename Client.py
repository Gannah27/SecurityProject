import socket
import clientchat
import pickle
import chatserver
import threading
from key_management_module import *


class Client(threading.Thread):
    def __init__(self, host='localhost', port=12345):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.csocket.connect((self.host, self.port))
        print("Connected to server")

    def receive(self):
        received_data = b""
        while True:
            try:
                data = self.csocket.recv(4096)
                if not data:
                    print("Connection closed")
                    break

                received_data += data
                if received_data:
                    keys = pickle.loads(received_data)
                    store_keys(keys, 'client_keys.txt')
                    print("Keys received and stored")
                    break
            except Exception as e:
                print(f"Error receiving data: {e}")
                break

    def send_credentials(self, username, password, req_type):
        data = f"{username},{password},{req_type}"
        self.csocket.send(data.encode())
        response = self.csocket.recv(1024).decode()
        print(f"[*] Received from server: {response}")
        return response


if __name__ == "__main__":

    newClient = Client()
    newClient.start()
    flag=0
    #j = threading.Thread(target=newClient.receive())
    #j.start()
    ans = input("Are you a new user? [y/n]: ")
    if ans == 'n':
        while True:
            username = input("Username: ")
            password = input("Password: ")
            response = newClient.send_credentials(username, password, 'verify')

            if response == "Log in successful":

                flag=1
                break
            else:
                print("Please re-enter your credentials.")
    elif ans == 'y':
        while True:
            username = input("Username: ")
            password = input("Password: ")
            response = newClient.send_credentials(username, password, 'add')
            if response == "Sign up successful":
                newClient.receive()
                flag=1
                break
            else:
                print("Email already exists, please enter another email.")
    if flag:
        key=distribute_keys("client_keys.txt")

        clientchat.Client(key).start_chat()