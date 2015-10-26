#!/bin/bash
if [ "$#" -ne 3 ]; then
	echo "Incorrect usage\n"
	echo "Usage: sudo sh client_tunnel.sh <path_to_private_key> <private_ip_host> <private_ip_cloud_server>"
	exit 1
fi
# Connect via ssh to external host and create a tunnel with the ssh connection
sudo ssh -i $1 -NTCf -vw 0:0 ec2-54-149-41-2.us-west-2.compute.amazonaws.com; 
# Turn on tun0 interface
sudo ip link set tun0 up; 
# Create tunnel and specify own private ip address and connect it to external host
sudo ip addr add $2/32 peer $3 dev tun0; 
