import ipaddress

def subnetting(ip, hosts, network):
    # ip: a string representing the IPv4 address
    # hosts: an integer representing the number of hosts required in the subnet
    # network: an integer representing the network number of the subnet
    # returns: a tuple of strings containing the subnet mask, network class, network address, broadcast address and usable address range

    # create an IPv4Interface object from the ip and network
    iface = ipaddress.ip_interface(f"{ip}/{network}")

    # get the IPv4Network object from the interface
    net = iface.network

    # get the prefix length from the network
    prefix = net.prefixlen

    # get the netmask from the network
    netmask = net.netmask

    # get the network class from the first octet of the ip
    first_octet = int(ip.split(".")[0])
    if first_octet < 128:
        net_class = "A"
    elif first_octet < 192:
        net_class = "B"
    elif first_octet < 224:
        net_class = "C"
    elif first_octet < 240:
        net_class = "D"
    else:
        net_class = "E"

    # get the network address from the network
    net_address = net.network_address

    # get the broadcast address from the network
    broadcast_address = net.broadcast_address

    # get the usable address range from the network
    # exclude the network and broadcast addresses
    usable_hosts = list(net.hosts())
    if len(usable_hosts) > 0:
        first_usable = usable_hosts[0]
        last_usable = usable_hosts[-1]
        usable_range = f"{first_usable} - {last_usable}"
    else:
        usable_range = "None"

    # return the output as a tuple of strings
    return (str(netmask), net_class, str(net_address), str(broadcast_address), usable_range)

store = subnetting("192.168.1.0", 5, 1)

print(store)
print("Subnetted!")