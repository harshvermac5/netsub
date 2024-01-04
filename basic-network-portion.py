def get_network_portion(ip_address, subnet_choice, subnet_prefix=None):
    # Split the IP address into octets
    octets = ip_address.split('.')

    # Convert each octet to binary
    binary_octets = [format(int(octet), '08b') for octet in octets]

    # Concatenate the binary octets
    binary_ip = ''.join(binary_octets)

    # Determine the subnet prefix based on user choice
    if subnet_choice == 'classful':
        # Determine the default subnet prefix based on the IP address class
        if int(octets[0]) <= 127:
            subnet_prefix = 8
        elif int(octets[0]) <= 191:
            subnet_prefix = 16
        else:
            subnet_prefix = 24

    # Get the network portion based on the chosen subnet prefix
    network_portion = binary_ip[:subnet_prefix]

    # Pad with zeros to get a complete octet
    network_portion += '0' * (32 - subnet_prefix)

    # Split the binary network portion into octets
    network_octets = [network_portion[i:i + 8] for i in range(0, 32, 8)]

    # Convert each octet back to decimal
    network_address = '.'.join(str(int(octet, 2)) for octet in network_octets)

    return network_address

# Example usage
ip_address = input("Enter the IPv4 address: ")
subnet_choice = input("Choose subnet type ('classful' or 'custom'): ")

if subnet_choice == 'custom':
    subnet_prefix = int(input("Enter the subnet prefix length: "))
else:
    subnet_prefix = None

network_portion = get_network_portion(ip_address, subnet_choice, subnet_prefix)
print(f"The network portion of {ip_address}/{subnet_prefix} is: {network_portion}")
