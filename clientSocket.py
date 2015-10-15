import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'ec2-54-186-193-51.us-west-2.compute.amazonaws.com'
port = 6325

#Connect to remote server
s.connect((host , port))
 
print 'Socket Connected to ' + host 

message = "jeff test"

try:
	s.sendall(message)
except socket.error:
	print "Error sending message"
	s.close
	sys.exit()

print 'Message sent successfully'

try:
	reply = s.recv(4096)
except socket.error:
	print "Error receiving respone"
	s.close
	sys.exit()

print "Received " + reply + " from remote host"

s.close()