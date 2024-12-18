import socket  
# take the server name and port name   
host = 'localhost' 
port = 5003   
# create a socket at client side  using TCP / IP protocol 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   
# connect it to server and port number on local computer. 
s.connect(('127.0.0.1', port)) 
print("Enter the message to the server") 
clientmsg=input() 
s.send(clientmsg.encode())# client is sending hello 
# receive message string from server, at a time 1024 B 
msg = s.recv(1024)  #receiving server message 
print('Received from server') 
print(msg.decode()) # displaying received message 
# disconnect the client 
s.close()