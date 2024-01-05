from tkinter import *

window = Tk()
window.title("IPv6 Address Generator")
window.geometry("400x200")

# Global Routing Prefix
global_routing_prefix_label = Label(window, text="Global Routing Prefix")
global_routing_prefix_label.grid(column=0, row=0)

global_routing_prefix_entry = Entry(window, width=30)
global_routing_prefix_entry.grid(column=1, row=0)

# MAC Address
mac_address_label = Label(window, text="MAC Address")
mac_address_label.grid(column=0, row=1)

mac_address_entry1 = Entry(window, width=4)
mac_address_entry1.grid(column=1, row=1)

mac_address_entry2 = Entry(window, width=4)
mac_address_entry2.grid(column=2, row=1)

mac_address_entry3 = Entry(window, width=4)
mac_address_entry3.grid(column=3, row=1)

mac_address_entry4 = Entry(window, width=4)
mac_address_entry4.grid(column=4, row=1)

mac_address_entry5 = Entry(window, width=4)
mac_address_entry5.grid(column=5, row=1)

mac_address_entry6 = Entry(window, width=4)
mac_address_entry6.grid(column=6, row=1)

# Generate Button
def generate_ipv6_address():
    global_routing_prefix = global_routing_prefix_entry.get()
    mac_address = mac_address_entry1.get() + mac_address_entry2.get() + mac_address_entry3.get() + mac_address_entry4.get() + mac_address_entry5.get() + mac_address_entry6.get()

    ipv6_address = generate_eui64_address(global_routing_prefix, mac_address)

    ipv6_address_label.configure(text=f"IPv6 Address: {ipv6_address}")

generate_button = Button(window, text="Generate", command=generate_ipv6_address)
generate_button.grid(column=0, row=2)

# IPv6 Address
ipv6_address_label = Label(window, text="IPv6 Address: ")
ipv6_address_label.grid(column=1, row=2)

window.mainloop()
