#!/usr/bin/python

"""
Simple HTTP Server version 2: reuses the port, so it can be
restarted right after it has been killed. Accepts connects from
the outside world, by binding to the primary interface of the host.

	Alejandro Valeriano Fernandez - GITT
	Ejercicio 14.2
	Server
"""

import random
import socket

# Create a TCP objet socket and bind it to a port
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to the main name of the host
mySocket.bind((socket.gethostname(), 1235))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an almost-infinite loop; the loop can be stopped with Ctrl+C)

try:
	while True:
		print 'Waiting for connections'
		(recvSocket, address) = mySocket.accept()
		print 'Request received:'
		print recvSocket.recv(2048)
		print 'Answering back...'
		randNum = str (random.randint (0,10000))

		recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
						"<html><body><h1>Hola. </h1>" + "<p><a href=" + randNum + ">Dame otra ''</a></p></body></html>\r\n")
		recvSocket.close()
except KeyboardInterrupt:
	print "Closing binded socket"
	mySocket.close()
