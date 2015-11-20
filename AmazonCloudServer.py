from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from urllib2 import urlopen
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
		self.new_instance_ip = None # just for debugging

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
	def get_ip(self):
		return self.new_instance_ip
	def list_instances(self):
		for inst in self.ec2.instances.all():
			if inst.public_ip_address != None:
				print("ID: "+inst.id+" TYPE: "+inst.instance_type+" STATE: "+inst.state['Name']+" Public DNS: "+inst.public_dns_name+" Public IP "+inst.public_ip_address)
	def create_instance(self):
		# If the GINI key does not exist, create it
		found_key = 0
		for key_info in self.ec2.key_pairs.all():
			if key_info.key_name == self.key_name:
				found_key = 1
				break
		if not found_key:
			self.key_gen()
		# This image ID is a special image that has the yRouter installed on it
		new_instance = self.ec2.create_instances(ImageId="ami-fa94859b", MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName = self.key_name, SecurityGroups = ['GINI',])	
		# Chill for that instance to be crafted
		while(new_instance[0].public_ip_address == None):
			new_instance[0].load()  # Get current status
			print("ID: "+new_instance[0].id+" State: "+new_instance[0].state['Name']+" No IP Address")
			time.sleep(5)
		# Need this newly created instances public IP address to set up the tunnel
		self.new_instance_ip = new_instance[0].public_ip_address 
	def stop_all_instances(self):
		for inst in self.ec2.instances.all():
			inst.stop()
	def terminate_all_instances(self):
		for inst in self.ec2.instances.all():
			inst.terminate()
	def terminate_instance(self, ip):
		for inst in self.ec2.instances.all():
			if inst.public_ip_address == ip:
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
	def create_tunnel(self):
		# need to copy the yRouter to the cloud
		print("Creating tunnel")
		# copy the cloud configuration file to the instance
		os.system("scp -i "+self.key_name+".pem -o StrickHostKeyChecking=no cloud_tunnel ubuntu@"+self.new_instance_ip)
		#start the cloud router
		# Note you have to delete the files it creates on the cloud after if you want to run it again
		os.system("xterm -e ssh -i GINI.pem -o StrictHostKeyChecking=no ubuntu@"+self.new_instance_ip+" 'source ~/.profile; yRouter/src/yrouter --interactive=1 --verbose=2 --confpath=/home/ubuntu --config=cloud_tunnel Router_1;exec bash'")
		#start the local router ...

	def create_tunnel_cloud_config_file(self):
		f = open("cloud_tunnel","w")
		print("Trying to get public ip")
		local_ip = urlopen('http://ip.42.pl/raw').read() # Get local public IP
		print("Got public ip")
		ifconfig = "ifconfig add tun0 -dstip "+local_ip+" -dstport 1 -addr "+local_ip+" -hwaddr a0:a0:a0:a0:a0\n"
		f.write(ifconfig)
		route = "route add -dev tun0 -net "+local_ip+" -netmask 255.255.255.255\n"
		f.write(route)
		f.close()

	def create_tunnel_local_config_file(self):
		if self.new_instance_ip == None:
			print("Create an instance first!")
			return
		f = open("local_tunnel","w")
		ifconfig = "ifconfig add tun0 -dstip "+self.new_instance_ip+" -dstport 1 -addr "+self.new_instance_ip+" -hwaddr a1:a1:a1:a1:a1\n"
		f.write(ifconfig)
		route = "route add -dev tun0 -net "+self.new_instance_ip+" -netmask 255.255.255.255\n"
		f.write(route)
		f.close()



server.register_instance(AmazonCloudFunctions())

print("Serving on 8000")
# Run the server's main loop
server.serve_forever()



