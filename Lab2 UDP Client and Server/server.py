from socket import *
import random 
import time 

#setting the same port number as the client side.
#creating socket
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

# assign server port number 12000 to the server's socket.
serverSocket.bind(('', serverPort))
print('The server is ready to receive')

# in the while loop, UDPServer waits for a packet to arrive.
# receives encrypted message and send it back to client.
while 1 :

# Message: when packet arrived, it is put into the variable message.
# clientAddress: when packet arrived, packet's source address is put into the clientaddress.
# buffer size is 1024
	message, clientAddress = serverSocket.recvfrom(2048)

	#adding delay between 5ms to 50ms
	time.sleep(random.uniform(0.005,0.05)) 

	#10% failure rate
	#no response to client if packet gets lost.
	failure_rate=random.randint(1,10)
	if failure_rate == 10:
		pass
	else:
		serverSocket.sendto(message, clientAddress)
	
	





