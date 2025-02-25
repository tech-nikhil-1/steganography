import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np

global img_path
img_path = ""

def select_image():
    global img_path
    img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png")])
    if img_path:
        browse_label.config(text=f"Selected: {img_path}")

def encrypt_message():
    global img_path
    if not img_path:
        messagebox.showerror("Error", "Please select an image!")
        return
    
    img = cv2.imread(img_path)
    msg = msg_entry.get("1.0", tk.END).strip()  # Fetch text properly from Text widget
    password = pass_entry.get()
    
    if not msg or not password:
        messagebox.showerror("Error", "Message and password cannot be empty!")
        return
    
    msg = password + '|' + msg + chr(0)  # Embed password and message with a null terminator
    
    n, m, z = 0, 0, 0
    try:
        for char in msg:
            img[n, m, z] = ord(char)
            z = (z + 1) % 3
            if z == 0:
                m += 1
                if m >= img.shape[1]:
                    m = 0
                    n += 1
                    if n >= img.shape[0]:
                        messagebox.showerror("Error", "Message too long for the selected image!")
                        return
    except IndexError:
        messagebox.showerror("Error", "Message too long for this image!")
        return
    
    encrypted_path = os.path.abspath("encryptedImage.png")
    cv2.imwrite(encrypted_path, img)
    
    # Clear GUI and show the encrypted image and path
    for widget in root.winfo_children():
        widget.destroy()
    
    tk.Label(root, text=f"Encrypted Image Saved at:", font=("Arial", 14)).pack()
    tk.Label(root, text=encrypted_path, font=("Arial", 12), wraplength=350).pack()
    
    show_encrypted_image(encrypted_path)
    
    tk.Button(root, text="OK", font=("Arial", 12), command=root.quit).pack()

def show_encrypted_image(image_path):
    img = Image.open(image_path)
    img = img.resize((200, 200), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    img_label = tk.Label(root, image=img)
    img_label.image = img
    img_label.pack()

def decrypt_message():
    global img_path
    if not img_path:
        messagebox.showerror("Error", "Please select an image!")
        return
    
    img = cv2.imread(img_path)
    entered_pass = pass_entry.get()
    
    if not entered_pass:
        messagebox.showerror("Error", "Please enter the password!")
        return
    
    n, m, z = 0, 0, 0
    extracted_message = ""
    
    try:
        while True:
            char = chr(img[n, m, z])
            if char == chr(0):
                break
            extracted_message += char
            z = (z + 1) % 3
            if z == 0:
                m += 1
                if m >= img.shape[1]:
                    m = 0
                    n += 1
                    if n >= img.shape[0]:
                        break
        
        if '|' in extracted_message:
            stored_pass, decrypted_msg = extracted_message.split('|', 1)
            if stored_pass == entered_pass:
                # Adjust message box size to fit 3 lines with 5 words per line
                msg_box = tk.Toplevel(root)
                msg_box.title("Decrypted Message")
                text_widget = tk.Text(msg_box, font=("Arial", 14), width=30, height=5)
                text_widget.insert("1.0", decrypted_msg)
                text_widget.config(state="disabled")
                text_widget.pack(padx=20, pady=20)
                tk.Button(msg_box, text="OK", font=("Arial", 12), command=root.quit).pack()
            else:
                messagebox.showerror("Error", "Decryption failed. Invalid password.")
        else:
            messagebox.showerror("Error", "Decryption failed. No valid message found.")
    except Exception as e:
        messagebox.showerror("Error", "Decryption failed. Invalid image or password.")

def show_encryption_fields():
    browse_button.pack()
    browse_label.pack()
    msg_label.pack()
    msg_entry.pack()
    pass_label.pack()
    pass_entry.pack()
    proceed_button.config(text="Encrypt", command=encrypt_message)
    proceed_button.pack()

def show_decryption_fields():
    browse_button.pack()
    browse_label.pack()
    msg_label.pack_forget()
    msg_entry.pack_forget()
    pass_label.pack()
    pass_entry.pack()
    proceed_button.config(text="Decrypt", command=decrypt_message)
    proceed_button.pack()

def process_choice():
    browse_button.pack_forget()
    browse_label.pack_forget()
    msg_label.pack_forget()
    msg_entry.pack_forget()
    pass_label.pack_forget()
    pass_entry.pack_forget()
    proceed_button.pack_forget()
    
    choice = choice_var.get()
    if choice == "1":
        show_encryption_fields()
    elif choice == "2":
        show_decryption_fields()
    else:
        messagebox.showerror("Error", "Invalid choice! Select Encrypt or Decrypt.")

# GUI Setup
root = tk.Tk()
root.title("Image Steganography")
root.geometry("500x500")

choice_var = tk.StringVar()
tk.Label(root, text="Select an option:", font=("Arial", 12)).pack()
tk.Radiobutton(root, text="Encrypt", variable=choice_var, value="1", font=("Arial", 12)).pack()
tk.Radiobutton(root, text="Decrypt", variable=choice_var, value="2", font=("Arial", 12)).pack()
tk.Button(root, text="Proceed", font=("Arial", 12), command=process_choice).pack()

browse_button = tk.Button(root, text="Browse Image", font=("Arial", 12), command=select_image)
browse_label = tk.Label(root, text="No file selected", font=("Arial", 12))
msg_label = tk.Label(root, text="Enter Message:", font=("Arial", 12))
msg_entry = tk.Text(root, font=("Arial", 12), width=30, height=3)
pass_label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
pass_entry = tk.Entry(root, show="*", font=("Arial", 12))
proceed_button = tk.Button(root, font=("Arial", 12))

root.mainloop()
