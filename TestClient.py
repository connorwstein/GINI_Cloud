import xmlrpclib
import boto3
import time
import sys

s = xmlrpclib.ServerProxy('http://localhost:8000')

# could use sys.argv to get the keys from the command line
#note add your keys before running the test client
s.configure_aws("AKIAIM65WKOBI3B3ETKA","emIme22KJKEPwrNIVbZ4h+FLeUhDrwNgqKWt55su")
# s.list_instances()
# s.create_instance()
# s.list_instances()
s.create_tunnel_cloud_config_file()
s.create_tunnel_local_config_file()
#s.create_tunnel()


# Print list of available methods
print(s.system.listMethods())

# while True:
# 	key = raw_input(">>> 'exit' to terminate ")
# 	if key == 'exit':
# 		s.terminate_all_instances()