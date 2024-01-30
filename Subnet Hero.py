import tkinter as tk
from tkinter import *


def clear_frame():
    for widget in window.winfo_children():
        widget.destroy()





def screen_one(): #Home Screen
    clear_frame()
    label_1 = Label(window, text="Select the Type of\nAddress", font=("Fira Sans", 18))
    label_1.pack(pady=10)
    button_1 = tk.Button(text="IPv4", font=("Fira Sans Heavy", 36), command=lambda: screen_two())
    button_2 = tk.Button(text="IPv6", font=("Fira Sans Heavy", 36), command=lambda: screen_two())
    button_1.pack(padx=10, pady=10)
    button_2.pack(padx=10, pady=10)

def screen_two(): #IPv4 Screen
    clear_frame()
    label_2 = Label(window, text="IPv4 Subnetting", font=("Fira Sans", 18))
    label_3 = Label(window, text="Enter the IP Address", font=("Fira Sans", 14))
    label_4 = Label(window, text="Enter the CIDR", font=("Fira Sans", 14))
    label_5 = Label(window, text="Address Class", font=("Fira Sans", 14))
    label_6 = Label(window, text="Network Address(First Subnet)", font=("Fira Sans", 14))
    label_7 = Label(window, text="Broadcast Address (First Subnet)", font=("Fira Sans", 14))
    label_8 = Label(window, text="Number of Hosts Per Network", font=("Fira Sans", 14))
    label_9 = Label(window, text="Total number of Sub-Networks", font=("Fira Sans", 14))
    button_2 = Button(window, text="Back to main menu", command=lambda: screen_one())
    label_2.grid(row=1, column=1) #Header Field
    label_3.grid(row=2, column=1, sticky=tk.W)
    label_4.grid(row=3, column=1, sticky=tk.W)
    label_5.grid(row=4, column=1, sticky=tk.W)
    label_6.grid(row=5, column=1, sticky=tk.W)
    label_7.grid(row=6, column=1, sticky=tk.W)
    label_8.grid(row=7, column=1, sticky=tk.W)
    label_9.grid(row=8, column=1, sticky=tk.W)
    button_2.pack(pady=10)

def screen_three(): #IPv6 Screen
    clear_frame()
    label_2 = Label(window, text="IPv6 Subnetting", font=("Fira Sans", 18))
    button_2 = Button(window, text="Back to main menu", command=lambda: screen_one())
    label_2.pack(pady=10)
    button_2.pack(pady=10)



window = tk.Tk()
window.title("Subnet Hero")
window.geometry('640x320')

screen_one()
window.mainloop()