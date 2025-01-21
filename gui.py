import tkinter as tk
from tkinter import messagebox
from caesar_cipher import caesar_cipher_encrypt, caesar_cipher_decrypt

def perform_encryption():
    plaintext = input_text.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
        encrypted_text = caesar_cipher_encrypt(plaintext, shift)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, encrypted_text)
    except ValueError:
        messagebox.showerror("Error", "Shift must be an integer.")

def perform_decryption():
    ciphertext = input_text.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
        decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, decrypted_text)
    except ValueError:
        messagebox.showerror("Error", "Shift must be an integer.")

def reset_fields():
    # Clear all fields
    input_text.delete("1.0", tk.END)
    shift_entry.delete(0, tk.END)
    result_text.delete("1.0", tk.END)

# Create the main application window
root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("450x450")
root.config(bg="#474747")

# Title label
title_label = tk.Label(root, text="Caesar Cipher Encryption/Decryption", font=("Arial", 14, "bold"), bg="#474747", fg="white")
title_label.pack(pady=10)

# Input text field
input_label = tk.Label(root, text="Enter text:", font=("Arial", 12, "bold"), bg="#474747", fg="white")
input_label.pack(pady=5)
input_text = tk.Text(root, height=5, width=40)
input_text.pack(pady=5)

# Shift entry field
shift_label = tk.Label(root, text="Shift value:", font=("Arial", 12), bg="#474747", fg="white")
shift_label.pack(pady=5)
shift_entry = tk.Entry(root, width=10)
shift_entry.pack(pady=5)

# Encrypt, Decrypt, and Reset buttons
btn_frame = tk.Frame(root, bg="#474747")
btn_frame.pack(pady=10)

encrypt_button = tk.Button(btn_frame, text="Encrypt", font=("Arial", 10,"bold"),command=perform_encryption, bg="#27ae60", fg="white", width=12)
encrypt_button.grid(row=0, column=0, padx=5)

decrypt_button = tk.Button(btn_frame, text="Decrypt", font=("Arial", 10,"bold"), command=perform_decryption, bg="#c0392b", fg="white", width=12)
decrypt_button.grid(row=0, column=1, padx=5)

reset_button = tk.Button(btn_frame, text="Reset", font=("Arial", 10,"bold"), command=reset_fields, bg="#f39c12", fg="white", width=12)
reset_button.grid(row=0, column=2, padx=5)

# Result text field
result_label = tk.Label(root, text="Result:", font=("Arial", 12, "bold"), bg="#474747", fg="white")
result_label.pack(pady=5)
result_text = tk.Text(root, height=5, width=40)
result_text.pack(pady=5)

# Run the application
root.mainloop()
