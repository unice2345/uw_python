"""
echo client, usage:

 python echo_client.py <host> <port>

Both host and port are optional, defaults: localhost 50000
host must be present if you want to provide port
"""

import socket 
import sys
import select
import datetime

def prompt():
	sys.stdout.write('>')
	sys.stdout.flush() # force print of line without \n

host = 'localhost' 
port = 50004
size = 1024 

nargs = len(sys.argv)
if nargs > 1:
    host = sys.argv[1]
if nargs > 2:
    port = int(sys.argv[2])

server = socket.socket(socket.AF_INET, 
                  socket.SOCK_STREAM) 
server.connect((host,port)) 
print 'Connection accepted by (%s, %s)' % (host, port)
prompt()

timeout = 60 # seconds
input = [server, sys.stdin]
running = True 
while running:
	inputready, outputready, exceptready = select.select(input, [], [], timeout)
	
	# timeout
	if not inputready:
		print 'chat client running at %s' % datetime.datetime.now()
		prompt()
	for s in inputready:
		if s == sys.stdin:
			msg = sys.stdin.readline().strip('\n')
			if msg:
				server.send(msg)
			else:
				server.close()
				running = False
		elif s:
			data = server.recv(size)
			print data
			prompt()
server.close() 

