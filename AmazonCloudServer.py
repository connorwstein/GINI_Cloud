from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from subprocess import call
import os
import shutil
import boto3

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths=('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),requestHandler=RequestHandler, allow_none=True)
server.register_introspection_functions()

# Register pow() function; this will use the value of
# pow.__name__ as the name, which is just 'pow'.
# registering a built in function
# server.register_function(pow) 

# # Register a function under a different name
# def adder_function(x,y):
#     return x + y
# server.register_function(adder_function, 'add')

# # Register an instance; all the methods of the instance are
# # published as XML-RPC methods (in this case, just 'mul').
# class MyFuncs:
#     def mul(self, x, y):
#         return x * y

#Server dependencies awscli, boto3, python3


# When we init need to update the iptables on the machine
class AmazonCloudFunctions:
	def configure_aws(self,key,secret_key):
		#Create the .aws directory with the users keys (same functionality as aws configure)
		path=os.path.join(os.environ['HOME'],".aws")
		if os.path.exists(path):
			print("Directory exists, removing")
			shutil.rmtree(path)
		os.makedirs(path)
		creds=open(os.path.join(path,"credentials"),'w')
		config=open(os.path.join(path,"config"),'w')
		config.write('[default]\nregion = us-west2'); # default region
		creds.write('[default]\naws_access_key_id = '+key+'\naws_secret_access_key = '+secret_key);
		creds.close()
		config.close()
		self.ec2=boto3.resource('ec2') # ec2 now available for the other methods
	def list_instances():
		print("list")
	def create_instance():
		print("create")





server.register_instance(AmazonCloudFunctions())

print("Serving on 8000")
# Run the server's main loop
server.serve_forever()



