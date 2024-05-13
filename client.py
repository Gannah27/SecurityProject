import socket


def start(SERVER_HOST,SERVER_PORT):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    return client_socket
def verify(username,password):

    # Send two parameters to the server
    param1 = username
    param2 = password
    data = f"{param1},{param2},verify"
    client_socket.send(data.encode())

    # Receive a response from the server
    response = client_socket.recv(1024).decode()
    print(f"[*] Received from server: {response}")
    return response
def add(username,password):

    # Send two parameters to the server
    param1 = username
    param2 = password
    data = f"{param1},{param2},add"
    client_socket.send(data.encode())

    # Receive a response from the server
    response = client_socket.recv(1024).decode()
    print(f"[*] Received from server: {response}")
    return  response
if __name__ == "__main__":
    ans= input("Are you a new user?[y/n]")
    client_socket=start() #add port and ip
    if ans == 'n':
        while True:
            username=input("username")
            password=input("password")
            flag1 = verify(username,password)
            if (flag1):
                print("please renter your credentials:")

            else:
                break
    elif ans == 'y':
        while True:
            username = input("username")
            password = input("password")
            flag1 = add(username,password)
            if (flag1):
                print("email already exits, please enter other email:")
            else:
                break

    client_socket.close()