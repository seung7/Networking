# Lab2: UDP Pinger 
## Goal:
Create a simple UDP client/server program that communicates through my local machine.
## Detail requirements:
* The client sends a simple message to the server using UDP. The server listens on the UDP port 12000 and responds back by simply echoing the message.
* The client then repeats the above 9 more times (that is, we send 10 ping messages and calculate the corresponding 10 RTT values).
* To simulate variability of delay, the server program must randomly wait for some time between 5 to 50 ms before responding back.
* To simulate packet loss, the server must randomly ignore a message (i.e. not responding back) 10% of the time. If the client does not hear back within 1 sec it must print a ‘request timed out’ message.
