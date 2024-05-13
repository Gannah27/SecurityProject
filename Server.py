import socket
import authentication_module

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = socket.gethostname()
port = 12345


server_socket.bind((host, port))


server_socket.listen(5)

print("Server listening on {}:{}".format(host, port))

while True:

    client_socket, addr = server_socket.accept()
    print('Got connection from', addr)
    data = client_socket.recv(1024).decode()
    # Split the received data into two parameters
    username, password,type = data.split(',')
    response=""
    if type == "add":
       response= authentication_module.signup(username,password)
    elif type =="verify":
       response= authentication_module.login(username,password)

    client_socket.send(response.encode())




    client_socket.close()
