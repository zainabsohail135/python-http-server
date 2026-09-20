import os
import socket

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000
BASE_DIR = os.path.realpath('htdocs')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

while True:
    client_connection, client_address = server_socket.accept()

    request = client_connection.recv(1024).decode()
    print(request)

    # Parse the first line of the request to get the path
    headers = request.split('\n')
    filename = headers[0].split()[1]

    # The root path means "give me the default page"
    if filename == '/':
        filename = '/index.html'

    # Resolve the real location on disk, then make sure it's inside htdocs
    full_path = os.path.realpath(BASE_DIR + filename)

    if not full_path.startswith(BASE_DIR + os.sep):
        response = 'HTTP/1.0 403 FORBIDDEN\n\nForbidden'
    else:
        try:
            fin = open(full_path)
            content = fin.read()
            fin.close()
            response = 'HTTP/1.0 200 OK\n\n' + content
        except FileNotFoundError:
            response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'

    client_connection.sendall(response.encode())
    client_connection.close()