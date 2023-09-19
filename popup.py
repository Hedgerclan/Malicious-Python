import tkinter as tk
from tkinter import messagebox
import socket
import uuid

def export_data():
    # Get the IP address, MAC address, and computer name
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    mac = ':'.join(['{:02X}'.format((uuid.getnode() >> elements) & 0xFF) for elements in range(0, 2 * 6, 2)][::-1])
    computer_name = hostname

    # Create a .txt file and write the data
    with open("system_info.txt", "w") as file:
        file.write(f"IP Address: {ip_address}\n")
        file.write(f"MAC Address: {mac}\n")
        file.write(f"Computer Name: {computer_name}\n")

    messagebox.showinfo("Export Data", "Data exported to system_info.txt")

def show_popup():
    message = "buttons"
    messagebox.showinfo("Popup Title", message)

def show_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    messagebox.showinfo("IP Address", f"Your IP Address: {ip_address}")

def show_computer_name():
    hostname = socket.gethostname()
    messagebox.showinfo("Computer Name", f"Your Computer Name: {hostname}")

def show_mac_address():
    mac = ':'.join(['{:02X}'.format((uuid.getnode() >> elements) & 0xFF) for elements in range(0,2*6,2)][::-1])
    messagebox.showinfo("MAC Address", f"Your MAC Address: {mac}")

# Create the main application window
root = tk.Tk()
root.title("Python Popup Example")

# Create a larger text area for the initial popup message
message_label = tk.Label(root, text="This is an initial larger popup message.\nYou can customize the message here.")
message_label.pack(pady=20)

# Create a button to trigger data export
export_button = tk.Button(root, text="Export Data", command=export_data)
export_button.pack()

# Create buttons for IP Address, Computer Name, and MAC Address with spacing
ip_button = tk.Button(root, text="IP Address", command=show_ip_address)
ip_button.pack(pady=10)
computer_name_button = tk.Button(root, text="Computer Name", command=show_computer_name)
computer_name_button.pack(pady=10)
mac_address_button = tk.Button(root, text="MAC Address", command=show_mac_address)
mac_address_button.pack(pady=10)

# Run the application
root.mainloop()
