from socket import *

address_family = AF_INET
socket_protocol = SOCK_STREAM
default_address = "0.0.0.0"
default_port = 80
default_capacity = 5


def start_server(socket, ip_address, start_port):
    """
        This function creates the server on the specified network interface 
        (ip_address) using the socket on the closest port to the start port.
    """
    while True:
        try:
            socket.bind((ip_address, start_port))
            break
        except:
            start_port+=1
    return socket, ip_address, start_port


server_socket, server_address, server_port= start_server(socket(address_family, socket_protocol), default_address, default_port)
server_socket.listen(default_capacity)
print("Server up at:")
print(server_address)
print(server_port)

