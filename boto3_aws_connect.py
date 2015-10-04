import boto3
import sys


def main():
	# 1. Need to run $ aws configure
	# and add API keys and the region
	# 2. Can create Linux AMI from an instance in the console, register that image
	# and use that image ID below
	ec2=boto3.resource('ec2')
	imageID=raw_input("Enter Linux HVM Image ID To Create an Instance\n")
	ec2.create_instances(ImageId=imageID, MinCount=1, MaxCount=1, InstanceType='t2.micro') # Must be t2.micro for a Linux HVM

if __name__=="__main__":main()



