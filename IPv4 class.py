import ipaddress

class IPv4SubnetInfo:
    def __init__(self, ip_address, cidr_notation):
        self.ip_address = ipaddress.IPv4Address(ip_address)
        self.network = ipaddress.IPv4Network(f"{ip_address}/{cidr_notation}", strict=False)

    def get_address_class(self):
        first_octet = int(str(self.ip_address).split('.')[0])
        if 1 <= first_octet <= 126:
            return 'A'
        elif 128 <= first_octet <= 191:
            return 'B'
        elif 192 <= first_octet <= 223:
            return 'C'
        elif 224 <= first_octet <= 239:
            return 'D'
        elif 240 <= first_octet <= 255:
            return 'E'
        else:
            return 'Invalid'
        
    def get_default_class(self):
        address_class = self.get_address_class()
        if address_class == 'A':
            return '255.0.0.0'
        elif address_class == 'B':
            return '255.255.0.0'
        elif address_class == 'C':
            return '255.255.255.0'
        elif address_class == 'D':
            return 'Not Applicable (Class D is reserved for multicast)'
        elif address_class == 'E':
            return 'Not Applicable (Class E is reserved for experimental)'
        else:
            return 'Invalid'
        
    def get_first_subnet_network_address(self):
        return str(self.network.network_address)

    def get_first_subnet_broadcast_address(self):
        subnet_mask = (2 ** (32 - self.network.prefixlen)) - 1
        return str(self.network.network_address + subnet_mask - 1)

    def get_hosts_per_network(self):
        return self.network.num_addresses - 2  # Exclude network and broadcast addresses

    def get_total_networks(self):
        return 2 ** (32 - self.network.prefixlen)
    
    def get_network_bits(self):
        return self.network.prefixlen

    def get_host_bits(self):
        return 32 - self.network.prefixlen

# Example usage:
ip_address = "128.0.0.3"
cidr_notation = 16
subnet_info = IPv4SubnetInfo(ip_address, cidr_notation)

# Get information
address_class = subnet_info.get_address_class()
first_subnet_network = subnet_info.get_first_subnet_network_address()
first_subnet_broadcast = subnet_info.get_first_subnet_broadcast_address()
default_class = subnet_info.get_default_class()
bits_in_network_part = subnet_info.get_network_bits()
bits_in_host_part = subnet_info.get_host_bits()
hosts_per_network = subnet_info.get_hosts_per_network()
total_networks = subnet_info.get_total_networks()

# Print or share this valuable info with your network! #IPv4 #Networking #Python

print(address_class, first_subnet_network, first_subnet_broadcast, default_class, bits_in_network_part, bits_in_host_part, hosts_per_network, total_networks)
