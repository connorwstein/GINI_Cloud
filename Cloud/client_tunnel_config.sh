#!/bin/bash

# Allow IP forwarding on your machine /proc/sys/net/ipv4/ip_forward
echo 1 | tee /proc/sys/net/ipv4/ip_forward;
# Configure /etc/sshd_config to allow tunneling 
echo 'PermitTunnel yes' >> /etc/ssh/sshd_config;

