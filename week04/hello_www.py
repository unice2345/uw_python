"""
hello_www.py - minimal web server + web application
"""

import socket
import sys

page = """
HTTP/1.0 200 OK
Content-Type text/html

<html>
<body>
Hello, world!
</body>
</html>
"""

host = ''
port = 8081

if len(sys.argv) > 1:
	port = int(sys.argv[1])

backlog = 5
size = 1024

# server's listener socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Release listener socket immediately when program exits,
# avoid socket error: [Error 48] Address already in use
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host, port))

print 'hello_www listening on port', port
s.listen(backlog)

while True:
	client, address = s.accept()
	request_data = client.recv(size)
	if request_data:
		print request_data
	client.send(page)
	client.close()
