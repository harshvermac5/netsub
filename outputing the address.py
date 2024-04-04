import ipaddress

def calculate_subnet_addresses(ip_address, subnet_mask, subnet_number):
    # Parse the IP address and subnet mask
    network = ipaddress.IPv4Network(ip_address + '/' + subnet_mask, strict=False)
    
    # Calculate the subnet size based on the subnet mask
    subnet_size = 2**(32 - int(subnet_mask))
    
    # Calculate the network address of the specified subnet
    network_address = str(network.network_address + subnet_size * (subnet_number - 1))
    
    # Calculate the broadcast address of the specified subnet
    broadcast_address = str(ipaddress.IPv4Address(network_address) + subnet_size - 1)

    # Calculate the number of hosts per subnet
    num_hosts_per_subnet = subnet_size - 2
    
    # Determine the class of the network
    network_class = determine_network_class(network.network_address)
    
    # Calculate the total number of subnets
    total_subnets = calculate_total_subnets(network_class, subnet_mask)
    
    return network_address, broadcast_address, total_subnets, num_hosts_per_subnet, network_class

def determine_network_class(network_address):
    first_octet = network_address.packed[0]
    if first_octet < 128:
        return 'A'
    elif first_octet < 192:
        return 'B'
    elif first_octet < 224:
        return 'C'
    elif first_octet < 240:
        return 'D'
    else:
        return 'E'

def calculate_total_subnets(network_class, subnet_mask):
    num_of_subnets = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]
    
    if network_class in {"A", "B", "C"}:
        return num_of_subnets[int(subnet_mask) - 17] if network_class == "B" else num_of_subnets[int(subnet_mask) - 25]
    elif network_class == "D":
        return None  # Class D is reserved for multicast addresses
    elif network_class == "E":
        return None  # Class E is reserved for experimental use
    else:
        return None  # Invalid network class


# Example usage:
ip_address = "192.168.0.0"
subnet_mask = "26"
subnet_number = 2
network_address, broadcast_address, total_subnets, num_hosts_per_subnet, network_class = calculate_subnet_addresses(ip_address, subnet_mask, subnet_number)
print("Network Address:", network_address)
print("Broadcast Address:", broadcast_address)
print("Total Number of Subnets:", total_subnets)
print("Number of Hosts per Subnet:", num_hosts_per_subnet)
print("Class of the Network:", network_class)
