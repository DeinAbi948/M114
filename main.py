import tkinter as tk
from tkinter import messagebox


class EncryptionApp:
    def __init__(self, root):
        self.root = root
        self.input_text_widget = None
        self.output_text_widget = None

    def encrypt_text(self):
        input_text = self.input_text_widget.get("1.0", "end-1c")
        key = 3  # Verschiebigsschlüssel
        encrypted_text = self.caesar_encrypt(input_text, key)
        self.output_text_widget.delete("1.0", "end")
        self.output_text_widget.insert("1.0", encrypted_text)

    def decrypt_text(self):
        input_text = self.input_text_widget.get("1.0", "end-1c")
        key = 3
        decrypted_text = self.caesar_decrypt(input_text, key)
        self.output_text_widget.delete("1.0", "end")
        self.output_text_widget.insert("1.0", decrypted_text)

    def create_encrypt_page(self):
        encrypt_page = tk.Toplevel(self.root)
        encrypt_page.title("Encrypt")
        encrypt_page.geometry("300x300")

        input_label = tk.Label(encrypt_page, text="Enter the text to encrypt:")
        input_label.pack()

        self.input_text_widget = tk.Text(encrypt_page, height=5, width=30)
        self.input_text_widget.pack()

        encrypt_button = tk.Button(encrypt_page, text="Encrypt", command=self.encrypt_text)
        encrypt_button.pack()

        output_label = tk.Label(encrypt_page, text="Encrypted Text:")
        output_label.pack()

        self.output_text_widget = tk.Text(encrypt_page, height=5, width=30)
        self.output_text_widget.pack()

    def create_decrypt_page(self):
        decrypt_page = tk.Toplevel(self.root)
        decrypt_page.title("Decrypt")
        decrypt_page.geometry("300x300")

        input_label = tk.Label(decrypt_page, text="Enter the encrypted text:")
        input_label.pack()

        self.input_text_widget = tk.Text(decrypt_page, height=5, width=30)
        self.input_text_widget.pack()

        decrypt_button = tk.Button(decrypt_page, text="Decrypt", command=self.decrypt_text)
        decrypt_button.pack()

        output_label = tk.Label(decrypt_page, text="Decrypted Text:")
        output_label.pack()

        self.output_text_widget = tk.Text(decrypt_page, height=5, width=30)
        self.output_text_widget.pack()

    def start_menu(self):
        self.start_menu = tk.Toplevel(self.root)
        self.start_menu.title("Start Menu")
        self.start_menu.geometry("300x150")

        welcome_label = tk.Label(self.start_menu, text="Welcome to the Encryption/Decryption Program!")
        welcome_label.pack()

        choice_label = tk.Label(self.start_menu, text="Please choose an option:")
        choice_label.pack()

        encrypt_button = tk.Button(self.start_menu, text="Encrypt", command=self.create_encrypt_page)
        encrypt_button.pack()

        decrypt_button = tk.Button(self.start_menu, text="Decrypt", command=self.create_decrypt_page)
        decrypt_button.pack()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

    def caesar_encrypt(self, text, key):
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                encrypted_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        return encrypted_text

    def caesar_decrypt(self, text, key):
        decrypted_text = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                decrypted_char = chr((ord(char) - ascii_offset - key) % 26 + ascii_offset)
                decrypted_text += decrypted_char
            else:
                decrypted_text += char
        return decrypted_text


# Anpassige am GUI
root = tk.Tk()
root.title("Encryption/Decryption Program")
root.geometry("300x150")

app = EncryptionApp(root)

start_button = tk.Button(root, text="Start", command=app.start_menu)
start_button.pack()

root.protocol("WM_DELETE_WINDOW", app.on_closing)
root.mainloop()
