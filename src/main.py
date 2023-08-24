import socket

from request import Request
from router import handle_request

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080


def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen()
    print(f"✓ Server running on http://{SERVER_HOST}:{SERVER_PORT}.\n")

    while True:
        client_connection, client_address = server_socket.accept()

        # Receive and interpret an HTTP request
        request = client_connection.recv(1024).decode()
        request = Request.interpret_request(request)
        request.log()

        # Router calls requested route
        response = handle_request(request)
        client_connection.sendall(response)
        client_connection.close()

    server_socket.close()


if __name__ == '__main__':
    run_server()
