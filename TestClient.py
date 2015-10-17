import xmlrpclib
import boto3

s = xmlrpclib.ServerProxy('http://localhost:8000')
#note add your keys before running the test client
s.configureAWS(<KEY>,<SECRET KEY>);

# Print list of available methods
print(s.system.listMethods())