import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)

# print(type(serv))

serv.bind(('127.0.0.1', 8000))
serv.listen(10)

client_sock, client_url = serv.accept()

print('client socket: {}, client url: {}'.format(client_sock, client_url))

data = client_sock.recv(1024)
print('Received data: {}'.format(str(data, 'utf-8')))
client_sock.sendall(data)