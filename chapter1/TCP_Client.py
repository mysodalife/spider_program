import socket
# step1: create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# step2: connect the server
s.connect(('127.0.0.1', 9999))

# step3: start send and receive with server
print('-->> ' + s.recv(1024).decode('utf-8'))
s.send(b'Hello, I am a client')
print('-->>' + s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()