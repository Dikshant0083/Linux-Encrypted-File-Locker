from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

# Generate a key
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

# Load the existing key
def load_key():
    return open(KEY_FILE, "rb").read()

# Encrypt a file
def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(file_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted)
    print(f"{file_path} encrypted successfully.")

# Decrypt a file
def decrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)
    with open(file_path, "rb") as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(file_path, "wb") as dec_file:
        dec_file.write(decrypted)
    print(f"{file_path} decrypted successfully.")

# CLI interaction
def main():
    if not os.path.exists(KEY_FILE):
        generate_key()

    print("Welcome to Encrypted File Locker")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt a file? ").lower()

    file_path = input("Enter the file path: ")

    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    if choice == "e":
        encrypt_file(file_path)
    elif choice == "d":
        decrypt_file(file_path)
    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()
