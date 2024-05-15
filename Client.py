from key_management_module import *
import socket
import pickle
import threading
import clientchat
class Client(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.host = "localhost"  # Change this to the server's IP address if necessary
        self.port = 12345
        
        self.csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.csocket.connect((self.host, self.port))
        print("Connected to server")
    
    def run(self):
        received_data = b""
        while True:
            try:
                data = self.csocket.recv(2505)  # Receive data in chunks of 1024 bytes
                if not data:
                    print("Connection closed")
                    break
                
                keys = pickle.loads(data)
                received_data+=data
                
            except Exception as e:
                print("Error receiving data:", e)
                break
        self.csocket.close()
        store_keys(keys, 'client_keys.txt')

    def verify(self,username, password):

        # Send two parameters to the server
        param1 = username
        param2 = password
        data = f"{param1},{param2},verify"
        self.csocket.send(data.encode())

        # Receive a response from the server
        response = self.csocket.recv(1024).decode()
        print(f"[*] Received from server: {response}")
        return response

    def add(self,username, password):

        # Send two parameters to the server
        param1 = username
        param2 = password
        data = f"{param1},{param2},add"
        self.csocket.send(data.encode())

        # Receive a response from the server
        response = self.csocket.recv(1024).decode()
        print(f"[*] Received from server: {response}")
        return response


newClient = Client()
newClient.start()
ans = input("Are you a new user?[y/n]")
if ans == 'n':
    while True:
        username = input("username")
        password = input("password")
        flag1 = newClient.verify(username, password)
        if (flag1):
            print("please renter your credentials:")

        else:
            break
elif ans == 'y':
    while True:
        username = input("username")
        password = input("password")
        flag1 = newClient.add(username, password)
        if (flag1):
            print("email already exits, please enter other email:")
        else:
            break
