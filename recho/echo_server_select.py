
import select
import socket
import sys
import time
import datetime

host = ''
port = 50003

if len(sys.argv) > 1:
	port = int(sys.argv[1])

backlog = 5
size = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((host,port))

print 'echo_server listening on port %s, to exit type return ' % port
server.listen(backlog)

timeout = 10
input = [server, sys.stdin]
running = True
while running:
	inputready, outputready, exceptready = select.select(input, [], [], timeout)

	if not inputready:
		print 'Server running at %s' % datetime.datetime.now()

	for s in inputready:
		if s == server:
			client, address = server.accept()
			input.append(client)
			print 'accept connection from ', address	
		elif s == sys.stdin:
			junk = sys.stdin.readline()
			running = False
			print 'Input %s from stdin, exiting.' % junk.strip('\n')
		elif s:
			data = s.recv(size)
			print '%s: %s' % (s.getpeername(), data.strip('\n'))
			if data:
				s.send('unice2345: %s' % data)
			else:
				s.close()
				print 'closed connection'
				input.remove(s)
server.close()
