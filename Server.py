import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = socket.gethostname()
port = 12345


server_socket.bind((host, port))


server_socket.listen(5)

print("Server listening on {}:{}".format(host, port))

while True:

    client_socket, addr = server_socket.accept()
    print('Got connection from', addr)

    #send and receive between two clients



    client_socket.close()
