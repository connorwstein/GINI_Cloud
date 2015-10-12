from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from subprocess import call

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),requestHandler=RequestHandler)
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
class AmazonCloudFunctions:
	def testMultiply(self,x,y):
		return x*y	#hello world function 
	def configureAWS(key, secret_key):
		#TODO: Sets up the users AWS creditentials and region
		#so boto3 can be used
		#then call self.ec2=boto3.resource('ec2')
		#could just make a ~/.aws directory with the credentials
	def listInstances():
		#TODO: List all the instances available
	def createInstance():

	def startInstance():
		
	def stopInstance():

	def destroyInstance():

	def generateKeyPair():
		#TODO: Generates a key pair to be used for the ssh
	def sshToInstances(pem_file, public_dns):
		#TODO: Using the pem file, open up an ssh session with the instance
		#Note that the username is ec2-user


server.register_instance(AmazonCloudFunctions())

print("Serving on 8000")
# Run the server's main loop
server.serve_forever()



