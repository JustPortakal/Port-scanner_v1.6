import socket
import tkinter as tk

def is_port_open(ip_address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip_address, int(port)))  
    if result == 0:
        return True
    else:
        return False

def check_port():
    ip_address = ip_entry.get()
    port = port_entry.get()
    if is_port_open(ip_address, port):
        result_label.config(text=f'Port {port} on {ip_address} is open.')
    else:
        result_label.config(text=f'Port {port} on {ip_address} is closed.')

root = tk.Tk()
root.title("")
root.resizable(False,False)
root.geometry("200x180")
root.eval('tk::PlaceWindow . center')

ip_label = tk.Label(root, text="IP:")
ip_label.pack()
ip_entry = tk.Entry(root, width=28)
ip_entry.pack()

port_label = tk.Label(root, text="Port:")
port_label.pack()
port_entry = tk.Entry(root, width=21)
port_entry.pack()

check_button = tk.Button(root, text="Check", command=check_port)
check_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

result_label2 = tk.Label(root, text="Port Checker v1.6")
result_label2.pack(pady=2)

root.mainloop()
