# Lab4: TraceRoute 
## Goal:
Create a TraceRoute programs that displays RTT(round trip time) values for all bypassed routers to reach the destination router.

## Detail requirements:
* Use socket module
* Use ICMP protocol 
* It displays the routers' info along the way (one per line).
* It calculates and displays 3 RTT values (ms) for each router (on the same line as the router info). If an RTT cannot be calculated within 4 seconds (a timeout), it should display a * (asterisk) instead for the RTT value and move on.
* The maximum number of hopes in the path to search for the destination is 30 hops, after which (if reached) the program terminates with a message "max number of hops reached ... terminating". Otherwise, it terminates when it reaches the destination.
* A command line argument is used to provide to our program the hostname that we would like to apply trace route on. If no hostname is provided (that is, if it is omitted), www.ubc.ca is to be considered as the default. 
example: python3  myTraceRoute.py   www.google.ca

## A sample example:
traceroute for google.ca (172.217.3.195)
1        1.47        1.24          1.22          192.168.1.1 (192.168.1.1)
2        2.62        3.03          2.78         192.168.0.1 (192.168.0.1)
3        *            *                   *          
4      19.09        *               15.08     something.vc.shawcable.net (44.95.113.113)
5      44.43      19.68       17.10      rc4sj-pos0-8-5-0.cl.shawcable.net (66.163.76.66)
6      (the rest are omitted, similar to above)

## Note:
on MacOS and Linux, you need to run the above as sudo, so just add sudo at the beginning of the above.
on Windows, your network gateway firewall (or even your own computer firewall) may need to be set to allow the packets you generate/receive to go through. 
