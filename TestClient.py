import xmlrpclib
import boto3
import time
import sys

s = xmlrpclib.ServerProxy('http://localhost:8000')

# could use sys.argv to get the keys from the command line
#note add your keys before running the test client
s.configure_aws("AKIAIM65WKOBI3B3ETKA","emIme22KJKEPwrNIVbZ4h+FLeUhDrwNgqKWt55su")

# Print list of available methods
print(s.system.listMethods())

while True:
	key = raw_input(">>> ")
	if key == 'create':
		s.create_instance()
	if key == 'list':
		s.list_instances()
	if key == 'ip':
		print(s.get_ip())
	if key == 'open_cloud':
		s.create_tunnel_cloud_config_file()
		s.create_tunnel()
	if key == 'terminate':
		ip = raw_input(">>> ip address? ")
		s.terminate_instance(ip)