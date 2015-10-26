#!/bin/bash
if [ "$#" -ne 2 ]; then
	echo "Illegal usage";
	echo "Usage: sudo sh cloud_tunnel.sh <private_ip_cloud_server_end> <private_ip_other_end>";
	exit 1;
fi
# Activate tun0 interface
sudo ip link set tun0 up
# Set up point-to-point tunnel with another host at the other end of the tunnel
sudo ip addr add $1/32 peer $2 dev tun0

