import subprocess
import re
from ipaddress import ip_address, ip_network

# Function to get active network connections using the 'netstat' command
def get_active_connections():
    # Run the 'netstat -tun' command to get the list of active TCP/UDP network connections
    result = subprocess.run(['netstat', '-tun'], stdout=subprocess.PIPE)
    
    # Decode the command output from bytes to a string
    connections = result.stdout.decode('utf-8')
    
    # Parse the decoded output to extract active connections
    return parse_connections(connections)

# Function to parse the connections output and extract IP addresses
def parse_connections(connections):
    active_connections = []  # List to store active IP addresses
    lines = connections.split('\n')  # Split the output into lines
    
    # Iterate through each line of the output
    for line in lines:
        parts = re.split(r'\s+', line)  # Split each line into parts using whitespace
        
        # Check if the line has at least 6 parts and the fifth part is an IP address
        if len(parts) >= 6 and re.match(r'\d+\.\d+\.\d+\.\d+', parts[4]):
            ip_port = parts[4]  # Extract the IP address and port
            ip = ip_port.split(':')[0]  # Split to get only the IP address
            
            # Check if the IP address is not private
            if not is_private_ip(ip):
                active_connections.append(ip)  # Add the IP address to the list
    
    # Return the list of unique active IP addresses
    return list(set(active_connections))

# Function to check if an IP address is private
def is_private_ip(ip):
    # Define private IP networks to be exluded from the search after that
    private_networks = [
        ip_network('10.0.0.0/8'),
        ip_network('172.16.0.0/12'),
        ip_network('192.168.0.0/16')
    ]
    
    ip_addr = ip_address(ip)  # Convert the IP address to an ip_address object
    
    # Check if the IP address belongs to any of the private networks
    for network in private_networks:
        if ip_addr in network:
            return True  # Return True if the IP address is private
    
    return False  # Return False if the IP address is not private
