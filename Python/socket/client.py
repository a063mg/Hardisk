import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
client_sock.connect(('127.0.0.1', 8000))

client_sock.sendall(bytes(input('Enter your data: '), 'utf-8'))

data = client_sock.recv(1024)

client_sock.close()

print('Received: {}'.format(data))