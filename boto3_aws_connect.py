import boto3
import sys
from subprocess import call



def main():
	# 1. Need to run $ aws configure
	# and add API keys and the region
	# 2. Can create Linux AMI from an instance in the console, register that image
	# and use that image ID below
	
	ec2=boto3.resource('ec2')
	while True:
		command=raw_input(">>>")
		if command=="ssh":
			# Need to make a key pair for the instance online at the moment
			pathToKey=raw_input("Enter path to ssh key\n")
			dns=raw_input("Enter public dns\n")
			call(["ssh","-i",pathToKey, "ec2-user@"+dns])
		elif command=="ls":
			for i in ec2.instances.all():
				print("ID: "+i.id+" TYPE: "+i.instance_type+" STATE: "+i.state['Name']+" Public DNS: "+i.public_dns_name)
		elif command=="launch":
			imageID=raw_input("Enter Linux HVM Image ID\n")
			ec2.create_instances(ImageId=imageID, MinCount=1, MaxCount=1, InstanceType='t2.micro')
		elif command=="stop":
			instanceID=raw_input("Enter Instance ID\n")
			instance=ec2.Instance(instanceID)
			instance.stop()
		elif command=="start":
			instanceID=raw_input("Enter Instance ID\n")
			instance=ec2.Instance(instanceID)
			instance.start()



if __name__=="__main__":main()



