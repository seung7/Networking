"""
client_server_mp.py is created so that a SINGLE terminal can run both client.py, server.py file.
It utilizes Python's mutliprocessing feature.
"""
from socket import *
import random 
import time 
import multiprocessing as mp

from sqlalchemy import true

def server():
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

def client():
    count=10
    pingcount=0

    #127.0.0.1 is localhost
    serverName = '127.0.0.1' 
    serverPort = 12000

    #creating the client's socket, called client socket
    #AF_INET means using IPv4.
    #SOCK_DGRAM means using UDP socket.
    #socket.clientSocket = socket(socket.AF_INET,socket.SOCK_DGRAM) 
    clientSocket = socket(AF_INET,SOCK_DGRAM) 
    print("The client is ready to send messages")

    #if not getting responds within 1 second, it gets timeout and call 'except'
    clientSocket.settimeout(1)

    while count>0 :
        #measure the current time
        #message.encode() converts string type to byte type
        #sendto have destination address to the message.
        initial_time= str(time.time()) 
        clientSocket.sendto(initial_time.encode(),(serverName, serverPort))
        

        #printout the pingnumber
        pingcount+=1
        print("pingcount:",pingcount)
        
        try:
            #when a packet arrives from internet, it get saved at modifiedMessage.
            #serverAddress has server's IP address and portnumber.
            #2048 is the buffer size
            #decoded_Message converts type byte to type string
            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
            decoded_Message = modifiedMessage.decode()
            
            #RTT_time is calculated by subtracting current time by initial_time
            RTT_time =  time.time()-float(decoded_Message)
        
            print("One RTT took : ", RTT_time, "seconds")
        except:
            print("request timed out")
        
        count -=1

    #pause system for 10 seconds
    time.sleep(10)
    clientSocket.close()

if __name__ == "__main__":

    #Process p1 has a forever while loop. 
    #Therefore, it is set to daemon so that when the main process finished exeucting, it will be force terminated.
    p1=mp.Process(target=server)
    p1.daemon=true
    p1.start()

    #Process p2 should not prematurely terminated. Therefore, p2.join() is utilized to block the main process. 
    p2=mp.Process(target=client)
    p2.start()
    p2.join()

    print("End of main process")