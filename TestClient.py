import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print(s.testMultiply(2,3))

# Print list of available methods
print(s.system.listMethods())