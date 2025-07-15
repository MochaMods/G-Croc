import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

def send_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    try:
        subprocess.Popen(['croc', file_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
    except FileNotFoundError:
        messagebox.showerror("Error", "Croc is not installed or not in PATH.")

def receive_code():
    code = code_entry.get().strip()
    if not code:
        messagebox.showwarning("Warning", "Enter a Croc code to receive a file.")
        return
    try:
        subprocess.Popen(['croc', code], creationflags=subprocess.CREATE_NEW_CONSOLE)
    except FileNotFoundError:
        messagebox.showerror("Error", "Croc is not installed or not in PATH.")

# GUI
root = tk.Tk()
root.title("g-croc GUI")

send_btn = tk.Button(root, text="Send File", command=send_file)
send_btn.pack(padx=10, pady=10)

code_label = tk.Label(root, text="Enter Croc Code:")
code_label.pack()

code_entry = tk.Entry(root, width=40)
code_entry.pack(padx=10, pady=5)

receive_btn = tk.Button(root, text="Receive File", command=receive_code)
receive_btn.pack(padx=10, pady=10)

root.mainloop()

