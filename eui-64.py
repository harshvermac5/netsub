import tkinter as tk
from tkinter import Entry, Button, Text, Scrollbar

def generate_eui64_address():
    global_routing_prefix = prefix_entry.get()
    mac_address = mac_entry.get()

    cleaned_mac = mac_address.replace(':', '').lower()
    first_half = cleaned_mac[:6]
    second_half = cleaned_mac[6:]
    modified_mac = first_half + 'fffe' + second_half

    binary_mac = format(int(modified_mac, 16), '048b')
    inverted_mac = binary_mac[:7] + ('1' if binary_mac[7] == '0' else '0') + binary_mac[8:]
    modified_binary_mac = inverted_mac[:24] + '1111111111111110' + inverted_mac[40:]
    modified_hex_mac = hex(int(modified_binary_mac, 2))[2:]

    ipv6_address = global_routing_prefix + modified_hex_mac
    result_text.config(state=tk.NORMAL)
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, ipv6_address)
    result_text.config(state=tk.DISABLED)

# Create the main window
window = tk.Tk()
window.title("EUI-64 Address Generator")

# Create and place the widgets
tk.Label(window, text="Global Routing Prefix:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(window, text="MAC Address:").grid(row=1, column=0, padx=10, pady=10)

prefix_entry = Entry(window)
prefix_entry.grid(row=0, column=1, padx=10, pady=10)

mac_entry = Entry(window)
mac_entry.grid(row=1, column=1, padx=10, pady=10)

generate_button = Button(window, text="Generate IPv6 Address", command=generate_eui64_address)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_text = Text(window, height=2, width=40, wrap=tk.NONE, state=tk.DISABLED)
result_text.grid(row=3, column=0, columnspan=2, pady=10)

result_scrollbar = Scrollbar(window, command=result_text.yview)
result_scrollbar.grid(row=3, column=2, sticky='nsew')
result_text['yscrollcommand'] = result_scrollbar.set

# Start the Tkinter event loop
window.mainloop()
