from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import os
import shutil
import boto3

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths=('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),requestHandler=RequestHandler, allow_none=True)
server.register_introspection_functions()

#Server dependencies awscli, boto3, python3
class AmazonCloudFunctions:
	
	def __init__(self):
		self.instances = []
		self.key_pair = None
		self.key_name = "GINI"

	def configure_aws(self,key,secret_key):
		#Create the .aws directory with the users keys (same functionality as aws configure)
		path=os.path.join(os.environ['HOME'],".aws")
		if os.path.exists(path):
			print("Directory exists, removing")
			shutil.rmtree(path)
		os.makedirs(path)
		creds=open(os.path.join(path,"credentials"),'w')
		config=open(os.path.join(path,"config"),'w')
		config.write('[default]\nregion = us-west-2'); # default region
		creds.write('[default]\naws_access_key_id = '+key+'\naws_secret_access_key = '+secret_key);
		creds.close()
		config.close()
		ec2=boto3.resource('ec2') # ec2 now available for the other methods
		for inst in ec2.instances.all():
			self.instances.append(inst)
	def list_instances(self):
		for inst in self.instances:
			print("ID: "+inst.id+" TYPE: "+inst.instance_type+" STATE: "+inst.state['Name']+" Public DNS: "+inst.public_dns_name)
	def create_instance(self):
		# TODO Bernie create an image and then create a instance
	def stop_all_instances(self):
		for inst in self.instances:
			inst.stop()
	def start_all_instances(self):
		for inst in self.instances:
			inst.terminate()
	def key_gen(self):
    	self.key_pair=ec2.create_key_pair(False, self.key_name)
   		# f = open(key_name+".pem",'w')
     #    f.write(key_pair.key_material)
     #    f.close()
     #    os.chmod(f.name,0400)

server.register_instance(AmazonCloudFunctions())

print("Serving on 8000")
# Run the server's main loop
server.serve_forever()



