# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(('127.0.0.1', port))

data = ''

# receive data from the server
while True:
    if data == 'exit':
        s.close()
        break
    else:
        data = s.recv(1024).decode("utf-8")
        print(data)


