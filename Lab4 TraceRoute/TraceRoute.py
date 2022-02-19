#ELEC331 Assignment4
#Seungmin Lee #39572145

from socket import *
import time
import sys

#variables
#default url is ubc.ca
#ttl start from 1 and increased upto 30
serverPort = 33435
max_hops = 30
ttl =1
serverURL = 'ubc.ca'
RTT_time = [0,0,0]
counter = 0


# if the comand prompt's input is 2. (first input is the file name, second input is URL for testing)
# then the second input becomes new URL
if len(sys.argv) > 1:
    serverURL=(sys.argv[1])


#convert the URL to IP address
serverName=gethostbyname(serverURL)

print ("traceroute for %s (%s)" % (serverURL, serverName))

#while loop stop when ttl = 30, or destination address has arrived
while True:
    
    #each time, send packet for 3 times.
    for i in range(3):
        
        #receiver initialization
        #create the receiver Socket that takes ICMP
        #bind the receiver's socket to the port
        #setting up the timer for 4seconds
        receiverSocket = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP)
        receiverSocket.bind(('', serverPort))
        receiverSocket.settimeout(4)
        
        #client(= sender) initialization
        #create a client Socket that sends UDP
        #set up option so that it will have ttl information
        clientSocket = socket(AF_INET,SOCK_DGRAM, IPPROTO_UDP)
        clientSocket.setsockopt(SOL_IP, IP_TTL, ttl)
        
        #to measure RTT, start a timer
        initial_timer = time.time()
        
        #send an empty packet to the same Port that receiver is binded to
        clientSocket.sendto(b'',(serverName, serverPort))

        #when packet arrived, it's context is put into the emtpymessage
        #when packet arrived, packet's source is put into the router_address.
        
        #if packet arrived within 4seconds,
        #   packet's payload is putinto the emptymessage
        #   packet's source address (=router's address that dropped the packet due to ttl) is put into router_address
        #   RTT time is calculated in ms (microseconds)
        #if packet arrived after 4seconds,
        #   instead of RTT, '*' is assigned to RTT_time
        try:
            emptymessage, router_address = receiverSocket.recvfrom(1024)
            RTT_time[i] = (time.time()-initial_timer)*1000
        except:
            router_address = NULL
	RTT_time[i] = '*'
        
        #close the sockets
        clientSocket.close()
        receiverSocket.close()

    
    #output format is e.g #1  1.47  1.24  1.22  192.168.1.1(192.168.1.1)
    #   1. print #number
    output = '#{}  '.format(ttl)

    #   2. if RTT_time == *, printout type string,
    #      if RTT_time == number, printout type float with 2 decimal point
    if (type (RTT_time[0]).__name__ == 'str'):
        output += '{0!s}  '.format(RTT_time[0])
    else:
        output += '{:.2f}  '.format(RTT_time[0])
    if (type (RTT_time[1]).__name__ == 'str'):
        output += '{0!s}  '.format(RTT_time[1])
    else:
        output += '{:.2f}  '.format(RTT_time[1])
    if (type (RTT_time[2]).__name__ == 'str'):
        output += '{0!s}  '.format(RTT_time[2])
    else:
        output += '{:.2f}  '.format(RTT_time[2])

    #   3. Lastly printout router's IP
    output += '%s' % (router_address[0])
    print(output)


    #while loop stop when ttl = 30, or destination address has arrived
    ttl += 1
    if ttl == 31:
        print("ttl became 30. Traceroute is over")
        break
    
    if router_address[0] == serverName:
        print("Arrived to destination")
        break

    

