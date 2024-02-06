from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(10, 11))]
    password_numbers = [choice(numbers) for _ in range(randint(3, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(3, 4))]

    combined_lists = password_letters + password_numbers + password_symbols
    shuffle(combined_lists)
    final_password = ''.join(combined_lists)

    password_entry.insert(0, final_password)
    pyperclip.copy(final_password)


# # ----------------------------SEARCH FEATURE-------------------------------- #


def search():
    with open("data.json", "r") as data_file:
        user_accounts = json.load(data_file)
        website = website_entry.get().capitalize()
        try:
            users_search = user_accounts[website]
        except KeyError:
            messagebox.showerror(title="Not Found", message=f"Sorry, no entry for '{website}' found 😢")
        else:
            messagebox.showinfo(title="Here", message=f"Username: {users_search["email"]} \nPassword: {
                                users_search["password"]} \nYour password is ready to paste! ")
            pyperclip.copy(users_search["password"])


# # ---------------------------- SAVE PASSWORD ------------------------------- #


def save_entry():
    website = website_entry.get().capitalize()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,

        }
    }

    if len(website) > 0 and len(password) > 0:
        try:
            with open("data.json", "r") as data_file:
                # read/load data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update data with new data
            data.update(new_data)
            # Write new data to json file
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            messagebox.showinfo(title="Success", message="Your information was saved successfully!")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.delete(0, END)
    else:
        messagebox.showerror(title="Ooops", message="Oopsies...Looks like you didn't fill in all required info 😳")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=60, bg="black")

# backround image
canvas = Canvas(width=200, height=200, bg="black", highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Entry/label for web
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1)
web_lbl = Label(text="Website:", fg="white", bg="black", font=("Arial", 14))
web_lbl.grid(column=0, row=1)

# Entry/label for usrname/email_entry
email_entry = Entry(width=34)
email_entry.insert(0, "youremail@email.com")
email_entry.grid(column=1, row=2, columnspan=2)
email_entry_lbl = Label(text="Email:", fg="white", bg="black", font=("Arial", 14), pady=10)
email_entry_lbl.grid(column=0, row=2)

# Entry/label/button to create/generate password
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

password_entry_lbl = Label(text="Password:", fg="white", bg="black", font=("Arial", 14))
password_entry_lbl.grid(column=0, row=3)

generate_password_button = Button(text="Generate Password", width=12, activeforeground="blue", fg="black",
                                  highlightbackground="black", font=("Arial", 10), command=password_generator)
generate_password_button.grid(column=2, row=3)

# Add button
add_password = Button(text="Add", width=32, highlightbackground="black", activeforeground="blue", command=save_entry)
add_password.grid(column=1, row=4, columnspan=2)

# Search button
search_button = Button(text="Search", width=8, highlightbackground="black", activeforeground="blue",
                       command=search)
search_button.grid(column=2, row=1)



window.mainloop()
