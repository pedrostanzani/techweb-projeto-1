import socket
from pathlib import Path
from utils import extract_route, read_file, build_response
from routes import index

CUR_DIR = Path(__file__).parent
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080


def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen()
    print(f"✓ Server running on http://{SERVER_HOST}:{SERVER_PORT}.")

    while True:
        client_connection, client_address = server_socket.accept()

        # Receive and interpret an HTTP request
        request = client_connection.recv(1024).decode()
        print('*'*100)
        print(request)

        # Router calls requested route
        route = extract_route(request)
        filepath = CUR_DIR / route
        if filepath.is_file():
            response = build_response() + read_file(filepath)
        elif route == '':
            response = index(request)
        else:
            response = build_response(code=404)

        client_connection.sendall(response)
        client_connection.close()

    server_socket.close()


if __name__ == '__main__':
    run_server()
