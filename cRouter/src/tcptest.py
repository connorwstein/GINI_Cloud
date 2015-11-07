import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("142.157.109.100",60001))
s.listen(1)
conn,addr = s.accept()
print 'Connection address: ', addr
while 1:
	data = conn.recv(100)
	if not data: break
	print "received data:", data
	conn.send(data)  # echo
conn.close()







