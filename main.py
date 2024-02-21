# importing the tkinter module
from tkinter import *
from ipnetwork import *

# initialising the ui, by giving it size and title
window = Tk()
window.geometry("640x320")
window.title("Subnet Hero")

# function to switch screens
def clear_frame():
    for widget in window.winfo_children():
        widget.destroy()

# address type selection frame
def selection_menu():
    clear_frame()
    selection_lbl = Label(text="What kind of IP address you want to subnet?")
    selection_lbl.place(x=200, rely=0.2)
    ipv4_button = Button(text="IPv4 Addresses")
    ipv4_button.place(relx=0.5, rely=0.4, anchor=CENTER)
    ipv6_button = Button(text="IPv6 Addresses")
    ipv6_button.place(relx=0.5, rely=0.5, anchor=CENTER)

def ipv4_subnetting():
    clear_frame()
    variable = StringVar(window)
    variable.set("First")

    ipv4_label = Label(text="Enter the IPv4 Address")
    ipv4_label.place(x=10, rely=0.1)

    ipv4_entry = Entry()
    ipv4_entry.place(relx=0.4, rely=0.1)

    host_requirement = Label(text="How many host are required on subnet")
    host_requirement.place(x=10, rely=0.2)

    host_entry = Entry()
    host_entry.place(relx=0.4, rely=0.2)

    calculate = Button(text="Calculate", height=3, width=30)
    calculate.place(relx=0.6, rely=0.1)

    show_label = Label(text="Show")
    show_label.place(x=10, rely=0.4)

    show_network = OptionMenu(window, variable, "First", "Second", "Third", "Last")
    show_network.place(x=50, rely=0.4)

    network_label = Label(text="network")
    network_label.place(x= 140, rely=0.4)

    class_label = Label(text="Class")
    class_label.place(x= 255, rely=0.4)

    class_list = Listbox(height=1, width=4)
    class_list.place(x=300, rely=0.4)

    mask_used = Label(text="Mask used")
    mask_used.place(x=10, rely=0.3)

    mask_box = Listbox(height=1)
    mask_box.place(relx=0.4, rely=0.3)

    mask_cidr = Listbox(width=4, height=1)
    mask_cidr.place(relx=0.6, rely=0.3)

    network_add = Label(text="Network Address")
    network_add.place(x=10, rely=0.5)

    network_add_list = Listbox(height=1)
    network_add_list.place(relx=0.4, rely=0.5)

    broadcast_add = Label(text="Broadcast Address")
    broadcast_add.place(x=10, rely=0.6)

    broadcast_add_list = Listbox(height=1)
    broadcast_add_list.place(relx=0.4, rely=0.6)

    usable_add = Label(text="Usable Address Range")
    usable_add.place(x=10, rely=0.7)

    usable_add_list = Listbox(height=1)
    usable_add_list.place(relx=0.4, rely=0.7)
    



enter_ip_add = Label(text="Enter the IP Address")

# selection_menu()
ipv4_subnetting()

# putting window into mainloop
window.mainloop()