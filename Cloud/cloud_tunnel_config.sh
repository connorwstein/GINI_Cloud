#!/bin/bash
# Allow ip forwarding
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward;
# Configure /etc/sshd_config to allow tunneling: 
echo 'PermitTunnel yes' >> /etc/ssh/sshd_config;
# Configure /etc/ssh/sshd_config to allow root login:
echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config;
# Allow tcp forwarding
echo 'AllowTcpForwarding yes' >> /etc/ssh/sshd_config;
# Restart the ssh service to apply changes to ssh settings
sudo service sshd reload
# Configure /etc/sysctl.config to allow for ipv4 packet forwarding
sudo sysctl net.ipv4.conf.default.forwarding=1
#
