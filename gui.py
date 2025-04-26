import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

# Functions
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

def load_key():
    return open(KEY_FILE, "rb").read()

def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(file_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)
    with open(file_path, "rb") as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(file_path, "wb") as dec_file:
        dec_file.write(decrypted)

# GUI Application
def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        selected_file.set(file_path)

def encrypt_action():
    if not os.path.exists(KEY_FILE):
        generate_key()
    path = selected_file.get()
    if path:
        encrypt_file(path)
        messagebox.showinfo("Success", "File encrypted successfully!")
    else:
        messagebox.showerror("Error", "No file selected!")

def decrypt_action():
    if not os.path.exists(KEY_FILE):
        messagebox.showerror("Error", "Key file missing!")
        return
    path = selected_file.get()
    if path:
        decrypt_file(path)
        messagebox.showinfo("Success", "File decrypted successfully!")
    else:
        messagebox.showerror("Error", "No file selected!")

# Main GUI
app = tk.Tk()
app.title("Encrypted File Locker")

selected_file = tk.StringVar()

tk.Label(app, text="Select a file:").pack(pady=10)
tk.Entry(app, textvariable=selected_file, width=50).pack(pady=5)
tk.Button(app, text="Browse", command=select_file).pack(pady=5)

tk.Button(app, text="Encrypt", command=encrypt_action, bg="green", fg="white").pack(pady=10)
tk.Button(app, text="Decrypt", command=decrypt_action, bg="blue", fg="white").pack(pady=10)

app.geometry("400x250")
app.mainloop()
