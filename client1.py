import socket
c=socket.socket()
c.connect(('localhost',9992))
msg=input('enter your message')
c.send(bytes(msg,'utf-8'))
c.close()
