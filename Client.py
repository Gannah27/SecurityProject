from key_management_module import *
import socket
import pickle
import threading

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
                data = self.csocket.recv(2505)  # Receive data in chunks of 2505 bytes
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

newClient = Client()
newClient.start()