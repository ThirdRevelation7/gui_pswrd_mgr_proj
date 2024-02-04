from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


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


# # ---------------------------- SAVE PASSWORD ------------------------------- #


def save_entry():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    ok_to_save = messagebox.askokcancel(title="Details Entered", message=f"Your Entries \nWebsite: {
                                        website} \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

    if ok_to_save:
        if len(website) > 0 and len(password) > 0:
            with open("data.txt", "a") as file:
                file.write(f"Website: {website} | Email: {email} | Password: {password} \n ")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                email_entry.delete(0, END)
                email_entry.insert(0, "youremail@email.com")
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
website_entry = Entry(width=34)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)
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

generate_password_button = Button(text="Generate Password", width=12, activeforeground="blue",
                                  highlightbackground="black", fg="black", font=("Arial", 10), command=password_generator)
generate_password_button.grid(column=2, row=3)

# Add button
add_password = Button(text="Add", width=32, activeforeground="blue", command=save_entry)
add_password.grid(column=1, row=4, columnspan=2)


window.mainloop()
