import random
import string
import tkinter as tk
from tkinter import ttk
import pyperclip  

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    length = length_entry.get()
    if length.isdigit() and int(length) > 0:
        password = generate_password(int(length))
        password_var.set(password)
    else:
        password_var.set("Неверная длина. Пожалуйста, введите корректное число.")

def copy_to_clipboard():
    password = password_var.get()
    if password:
        pyperclip.copy(password)
        print("Пароль скопирован в буфер обмена")
    else:
        print("Сначала сгенерируйте пароль")

# Создание графического интерфейса
root = tk.Tk()
root.title("Password_generator")
root.geometry("200x200")

style = ttk.Style()
style.configure('TButton', font=('calibri', 10, 'bold'), foreground='dark blue')
style.configure('TLabel', font=('calibri', 10), foreground='black')

root.configure(bg='black')

length_label = ttk.Label(root, text="Длина пароля:")
length_label.pack()

length_entry = ttk.Entry(root)
length_entry.pack()

generate_button = ttk.Button(root, text="Сгенерировать", command=generate_and_display_password)
generate_button.pack()

copy_button = ttk.Button(root, text="Копировать пароль", command=copy_to_clipboard)
copy_button.pack()

password_var = tk.StringVar()
password_label = ttk.Label(root, textvariable=password_var)
password_label.pack()

root.mainloop()
