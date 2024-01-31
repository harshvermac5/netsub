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
    label_1 = Label(window, text="Subnet Hero", font=("Fira Sans", 18))
    label_2 = Label(window, text="IPv4 Address", font=("Fira Sans", 18))
    label_3 = Label(window, text="Number of Subnets", font=("Fira Sans", 18))
    label_4 = Label(window, text="Network Address (1st)", font=("Fira Sans", 18))
    label_5 = Label(window, text="Broadcast Address (1st)", font=("Fira Sans", 18))
    label_6 = Label(window, text="No. of hosts", font=("Fira Sans", 18))
    label_7 = Label(window, text="No. of Networks", font=("Fira Sans", 18))
    label_8 = Label(window, text="Network Class", font=("Fira Sans", 18))
    #label_9 = Label(window, text="Subnet ID", font=("Fira Sans", 18))
    #label_10 = Label(window, text="CIDR", font=("Fira Sans", 18))
    radio_1 = Radiobutton(window, text="Subnet ID", value=1, font=("Fira Sans", 18))
    radio_2 = Radiobutton(window, text="CIDR", value=2, font=("Fira Sans", 18))
    entry_1 = Entry(window)
    entry_2 = Entry(window)
    entry_3 = Entry(window)
    entry_4 = Entry(window)
    entry_5 = Entry(window)
    entry_6 = Entry(window)
    entry_7 = Entry(window)
    entry_8 = Entry(window)
    entry_9 = Entry(window)
    dot_1 = Label(window, text=".")
    dot_2 = Label(window, text=".")
    dot_3 = Label(window, text=".")
    dot_4 = Label(window, text=".")
    dot_5 = Label(window, text=".")
    dot_6 = Label(window, text=".")
    dot_7 = Label(window, text=".")
    dot_8 = Label(window, text=".")

    label_1.grid(row=1, column=1, columnspan=3)
    label_2.grid(row=2, column=1)
    radio_1.grid(row=3, column=1)
    radio_2.grid(row=4, column=1)
    label_3.grid(row=5, column=1)
    label_4.grid(row=6, column=1)
    label_5.grid(row=7, column=1)
    label_6.grid(row=8, column=1)
    label_7.grid(row=9, column=1)
    label_8.grid(row=10, column=1)
    entry_1.grid(row=3, column=2)
    dot_1.grid(row=3, column=3)
    entry_2.grid(row=3, column=4)

def screen_three(): #IPv6 Screen
    clear_frame()
    label_2 = Label(window, text="IPv6 Subnetting", font=("Fira Sans", 18))
    button_2 = Button(window, text="Back to main menu", command=lambda: screen_one())
    label_2.pack(pady=10)
    button_2.pack(pady=10)



window = tk.Tk()
window.title("Subnet Hero")
window.geometry()

screen_one()
window.mainloop()