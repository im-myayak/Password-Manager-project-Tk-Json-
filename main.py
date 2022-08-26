import json
import random
from tkinter import *
from tkinter import messagebox
import string
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = list(string.digits)
digits = list(string.ascii_letters)
symbol = "!@#$%^&*()"


def generate_password():

    pass_letters = [random.choice(letters) for i in range(random.randint(8, 10))]
    pass_digits = [random.choice(digits) for i in range(random.randint(2, 4))]
    pass_symbols = [random.choice(symbol) for i in range(random.randint(2, 4))]
    password = pass_letters + pass_digits + pass_symbols
    random.shuffle(password)
    g_password = "".join(password)
    password_entry.insert(0, g_password)
    pyperclip.copy(g_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #\


def Add():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    credentials_dict = {
        website:{
            "email_username": email_username,
            "password": password
        }
    }
    if not website_entry.get() or not password_entry.get():
        messagebox.showinfo(title="Oops", message="!!!PLease fill all the boxes!!!")
    else:
        try:
            with open("my_credentials.json", 'r') as file:
                data = json.load(file)
                data.update(credentials_dict)
        except FileNotFoundError:
            json.dump(credentials_dict, file, indent=4)
        else:
            data.update(credentials_dict)
            with open("my_credentials.json", "w") as file:
                json.dump(data, file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- Search credentials ------------------------------- #


def search_credentials():
    website = website_entry.get()
    try:
        with open("my_credentials.json") as file:
            credentials_dict = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Credentials", message="No Data File Found")
    else:
        if website in credentials_dict:
            email = credentials_dict[website]["email_username"]
            password = credentials_dict[website]["password"]

            messagebox.showinfo(title="Credentials", message=f"Email:{email}\nPassword:{password}")
            password_entry.insert(0, password)
        else:
            messagebox.showinfo(title="Credentials", message="No details for the website exists")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("PasswordGenerator")
window.config(padx=50, pady=50)

canvas = Canvas(window, width=200, height=200)
logo_Image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_Image)
canvas.grid(column=1, row=0)

website_label = Label(window, text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(window)
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()

search_button = Button(window, text="Search", command=search_credentials)
search_button.grid(column=2, row=1, sticky="EW")

email_username_label = Label(window, text="Email/Username:")
email_username_label.grid(column=0, row=2)
email_username_entry = Entry(window)
email_username_entry.insert(0, string="mykourouma32@gmail.com")
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_label = Label(window, text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(window)
password_entry.grid(column=1, row=3, sticky="EW")

generate_password_button = Button(window, text="Generate Password", command=generate_password, highlightthickness=0)
generate_password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(window, text="Add", command=Add, highlightthickness=0)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()
