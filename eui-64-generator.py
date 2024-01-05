def generate_eui64_address(global_routing_prefix, mac_address):
    # Remove any colons from the MAC address and convert to lowercase
    cleaned_mac = mac_address.replace(':', '').lower()

    # Split the MAC address into two halves
    first_half = cleaned_mac[:6]
    second_half = cleaned_mac[6:]

    # Insert 'fffe' in the middle of the MAC address
    modified_mac = first_half + 'fffe' + second_half

    # Convert the modified MAC address to binary
    binary_mac = format(int(modified_mac, 16), '048b')

    # Invert the 7th bit of the binary MAC address
    inverted_mac = binary_mac[:7] + ('1' if binary_mac[7] == '0' else '0') + binary_mac[8:]

    # Insert 'ff:fe' in the middle of the inverted binary MAC address
    modified_binary_mac = inverted_mac[:24] + '1111111111111110' + inverted_mac[40:]

    # Convert the modified binary MAC address back to hexadecimal
    modified_hex_mac = hex(int(modified_binary_mac, 2))[2:]

    # Concatenate the global routing prefix and modified EUI-64
    ipv6_address = global_routing_prefix + modified_hex_mac

    return ipv6_address

# Example usage
global_routing_prefix = input("Enter the global routing prefix of IPv6: ")
mac_address = input("Enter the MAC address of the interface: ")

ipv6_address = generate_eui64_address(global_routing_prefix, mac_address)
print(f"The generated IPv6 address is: {ipv6_address}")
