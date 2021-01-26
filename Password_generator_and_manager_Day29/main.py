from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(6, 8)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    [password_list.append(random.choice(letters)) for _ in range(0, nr_letters)]
    # for letter in range(0, nr_letters):
    #     password_list.append(random.choice(letters))

    [password_list.append(random.choice(numbers)) for _ in range(0, nr_numbers)]
    # for number in range(0, nr_numbers):
    #     password_list.append(random.choice(numbers))

    [password_list.append(random.choice(symbols)) for _ in range(0, nr_symbols)]
    # for number in range(0, nr_symbols):
    #     password_list.append(random.choice(symbols))

    # random.shuffle takes a list
    random.shuffle(password_list)
    password_string = ''.join(password_list)

    # convert a list to a string using join
    # print(password_string)
    password_entry.insert(0, password_string)
    # COpy to clipboard
    pyperclip.copy(password_string)
    generate_password_btn.configure(state='disabled')


# ---------------------------- PASSWORD MANAGER ------------------------------- #
def save_info():
    website = website_name_entry.get()
    email = user_info_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title='Empty fields', message='Please fill all fields before saving')
        return

    confirmed = messagebox.askokcancel(title='Confirm details', message=f"Website: {website}\n"
                                                                        f"Email: {email}\n"
                                                                        f"Password: {password}")
    if confirmed:
        user_details = f' {website}  | {email} | {password}'
        with open('data.txt', 'a') as file:
            file.write(user_details)
            file.write('\n')
        website_name_entry.delete(0, END)
        password_entry.delete(0, END)
    else:
        print('start again')

    generate_password_btn.configure(state='normal')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.configure(padx=100, pady=40, bg='#fff')
window.resizable(0, 0)

canvas = Canvas(height=200, width=200, highlightthickness=0)
password_bg = PhotoImage(file="logo1.png")
canvas.create_image(100, 100, image=password_bg)
canvas.grid(column=1, row=0)

website_name_label = Label(text='Website:', bg='#fff')
website_name_label.grid(column=0, row=1, sticky='W')

website_name_entry = Entry(bd=2, highlightthickness=0, relief='groove')
website_name_entry.focus()
website_name_entry.grid(column=1, columnspan=2, row=1, sticky='EW')

user_info_label = Label(text="Email/Username:", bg='#fff')
user_info_label.grid(column=0, row=2, pady=15, sticky='W')

user_info_entry = Entry(bd=2, highlightthickness=0, relief='groove')
user_info_entry.insert(0, 'user@gmail.com')
user_info_entry.grid(column=1, columnspan=2, row=2, sticky='EW')

password_label = Label(text="Password:", bg='#fff')
password_label.grid(column=0, row=3, sticky='W')

password_entry = Entry(bd=2, highlightthickness=0, relief='groove')
password_entry.grid(column=1, row=3, sticky='EW')

generate_password_btn = Button(text='Generate Password', relief='groove', command=generate_password)
generate_password_btn.grid(column=2, row=3, pady=1, sticky='EW')

add_btn = Button(text='Save', relief='groove', command=save_info)
add_btn.grid(column=1, columnspan=2, row=4, sticky='EW', pady=10)

window.mainloop()
