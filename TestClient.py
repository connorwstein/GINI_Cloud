import xmlrpclib
import boto3
import time
s = xmlrpclib.ServerProxy('http://localhost:8000')
#note add your keys before running the test client
s.configure_aws("AKIAIM65WKOBI3B3ETKA","emIme22KJKEPwrNIVbZ4h+FLeUhDrwNgqKWt55su")
s.list_instances()
s.create_instance()
s.list_instances()
# Print list of available methods
print(s.system.listMethods())