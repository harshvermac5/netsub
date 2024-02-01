import ipaddress

class SubnetCalculator:
    def __init__(self, ipv4_address, subnet_mask):
        self.ipv4_address = ipv4_address
        self.subnet_mask = subnet_mask
        self.network = ipaddress.IPv4Network(f"{ipv4_address}/{subnet_mask}", strict=False)

    def calculate_subnets(self):
        return self.network.num_addresses

    def calculate_first_subnet(self):
        first_subnet = str(self.network.network_address)
        broadcast_address = str(self.network.broadcast_address)
        return first_subnet, broadcast_address

    def get_address_class(self):
        first_octet = int(str(self.ipv4_address).split('.')[0])
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

# Example Usage:
ipv4_address = "192.168.1.0"
subnet_mask = "255.255.255.252"

calculator = SubnetCalculator(ipv4_address, subnet_mask)
num_subnets = calculator.calculate_subnets()
first_subnet_info = calculator.calculate_first_subnet()
address_class = calculator.get_address_class()
default_subnet = calculator.get_default_class()
network_bits = calculator.get_network_bits()
host_bits = calculator.get_host_bits()

# Unveil the power of networking: {num_subnets} subnets, with the first subnet ranging from {first_subnet_info[0]} to {first_subnet_info[1]}. 🌐✨ #NetworkingMagic #IPv4 #SubnetCalculator
print(num_subnets, first_subnet_info, address_class, default_subnet, network_bits, host_bits)
