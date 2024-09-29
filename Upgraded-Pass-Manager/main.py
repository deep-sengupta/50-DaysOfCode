from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)

def search_password():
    website = website_entry.get()
    password_entry.delete(0, END)
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            password_entry.insert(END, password)
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists!")

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=10, bg="white")

pass_manager_frame = Frame(window, bg="white")
pass_manager_frame.grid(row=0, column=0, columnspan=3, sticky="w", padx=(0, 0), pady=(10, 25))

pass_label = Label(pass_manager_frame, text="Pass", font=("Arial", 26, "bold"), fg="red", bg="white")
pass_label.pack(side="left")
manager_label = Label(pass_manager_frame, text="Manager", font=("Arial", 26, "bold"), fg="black", bg="white")
manager_label.pack(side="left")

window.grid_columnconfigure(1, weight=1)

website_label = Label(text="Website:", font=("Arial", 14), fg="black", bg="white", padx=5, pady=5, anchor="e")
website_label.grid(row=1, column=0, sticky="e")
email_label = Label(text="Email/Username:", font=("Arial", 14), fg="black", bg="white", padx=5, pady=5, anchor="e")
email_label.grid(row=2, column=0, sticky="e")
password_label = Label(text="Password:", font=("Arial", 14), fg="black", bg="white", padx=5, pady=5, anchor="e")
password_label.grid(row=3, column=0, sticky="e")

entry_style = {"font": ("Arial", 14), "fg": "black", "bg": "white", "insertbackground": "black", "highlightthickness": 1, "highlightbackground": "black", "highlightcolor": "black"}

website_entry = Entry(width=24, **entry_style)
website_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)
website_entry.focus()

email_entry = Entry(width=38, **entry_style)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w", padx=5, pady=5)

password_entry = Entry(width=24, **entry_style)
password_entry.grid(row=3, column=1, sticky="w", padx=5, pady=5)

button_style = {"fg": "black", "bg": "lightgrey", "activebackground": "lightgrey", "activeforeground": "black", "font": ("Arial", 12, "bold"), "borderwidth": 1, "relief": "solid", "highlightthickness": 0, "padx": 10, "pady": 5}

generate_password_button = Button(text="Generate Password", command=generate_password, **button_style)
generate_password_button.grid(row=3, column=2, padx=5, pady=5, sticky="w")

add_button = Button(text="Add", width=36, command=save, **button_style)
add_button.grid(row=4, column=1, columnspan=2, padx=5, pady=(10, 20), sticky="w")

search_button = Button(text="Search", width=14, command=search_password, **button_style)
search_button.grid(row=1, column=2, padx=5, pady=5, sticky="w")

window.mainloop()
