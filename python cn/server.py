import socket 
# take the server name and port name 
host = 'localhost' 
port = 5003 
# create a socket at server side using TCP / IP protocol 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
# bind the socket with server and port number 
s.bind(('', port))  
# allow maximum 1 connection to the socket 
s.listen(1) 
print("The server is ready to receive") 
# wait till a client accept connection 
c, addr = s.accept()   
# display client address 
print("CONNECTION FROM:", str(addr)) 
cmsg=c.recv(1024).decode() 
print("Message from client") 
print(cmsg)# displaying client message 
# send message to the client after encoding into binary string 
smsg="Hi" 
c.send(smsg.encode())  
# disconnect the server 
c.close()  