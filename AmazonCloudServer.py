from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import os
import shutil
import boto3
import time
# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths=('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),requestHandler=RequestHandler, allow_none=True)
server.register_introspection_functions()

#Server dependencies awscli, boto3, python3
class AmazonCloudFunctions:
	
	def __init__(self):
		self.key_pair = None
		self.key_name = "GINI"
		self.ec2 = None

	def configure_aws(self,key,secret_key):
		#Create the .aws directory with the users keys (same functionality as aws configure)
		path=os.path.join(os.environ['HOME'],".aws")
		if os.path.exists(path):
			print("Directory exists, removing")
			shutil.rmtree(path)
		os.makedirs(path)
		creds=open(os.path.join(path,"credentials"),'w')
		config=open(os.path.join(path,"config"),'w')
		config.write('[default]\nregion = us-west-2\n'); # default region
		creds.write('[default]\naws_access_key_id = '+key+'\naws_secret_access_key = '+secret_key+'\n');
		creds.close()
		config.close()
		self.ec2=boto3.resource('ec2') # ec2 now available for the other methods
	def list_instances(self):
		for inst in self.ec2.instances.all():
			print("ID: "+inst.id+" TYPE: "+inst.instance_type+" STATE: "+inst.state['Name']+" Public DNS: "+inst.public_dns_name)
	def create_instance(self):
		# If the GINI key does not exist, create it
		found_key = 0
		for key_info in self.ec2.key_pairs.all():
			if key_info.key_name == self.key_name:
				found_key = 1
				break
		if not found_key:
			self.key_gen()
		# This image ID is the default image file
		new_instance = self.ec2.create_instances(ImageId="ami-0211f431", MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName = self.key_name)	
		# Chill for that instance to be crafted
		while(new_instance[0].state['Name'] != "running"):
			new_instance[0].load()  # Get current status
			print("ID: "+new_instance[0].id+" State: "+new_instance[0].state['Name'])
			time.sleep(5) 
	def stop_all_instances(self):
		for inst in self.ec2.instances.all():
			inst.stop()
	def terminate_all_instances(self):
		for inst in self.ec2.instances.all():
			inst.terminate()
	def key_gen(self):
		# False means make the key for real
		self.key_pair = self.ec2.create_key_pair(DryRun = False, KeyName = self.key_name)
		if os.path.exists(self.key_name+".pem"):
			os.chmod(self.key_name+".pem",0777)
		f = open(self.key_name+".pem",'w')
		f.write(self.key_pair.key_material)
		f.close()
		os.chmod(f.name,0400)

server.register_instance(AmazonCloudFunctions())

print("Serving on 8000")
# Run the server's main loop
server.serve_forever()



