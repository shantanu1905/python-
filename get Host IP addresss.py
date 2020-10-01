# Import socket 
import socket

# To get the hostname by socket.gethostname() 
hostname = socket.gethostname()

# Getting the IP address using socket.gethostbyname() 
ip_address = socket.gethostbyname(hostname)

# Printing the hostname and ip_address

print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
