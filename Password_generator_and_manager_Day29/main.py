from tkinter import *
from tkinter import messagebox
import random
import pyperclip
from PIL import ImageTk, Image
import json


def open_window_one():
    # ---------------------------- PASSWORD GENERATOR ------------------------------- #
    def generate_password():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v',
                   'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R',
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

        data = {
            website: {
                "email": email,
                "password": password
            }
        }
        if len(website) == 0 or len(password) == 0:
            messagebox.showerror(title='Empty fields', message='Please fill all fields before saving')
            return

        try:
            with open('data.json', 'r') as file:
                # Read from file
                try:
                    retrieved_data = json.load(file)
                except json.decoder.JSONDecodeError:
                    retrieved_data = {}
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
        else:
            # Update with new data
            retrieved_data.update(data)
            # Write to file with the newly updated data
            with open('data.json', 'w') as file:
                json.dump(retrieved_data, file, indent=4)
        finally:
            website_name_entry.delete(0, END)
            password_entry.delete(0, END)

        generate_password_btn.configure(state='normal')

    def find_password():
        try:
            with open('data.json') as file:
                data_items = json.load(file)
        except FileNotFoundError:
            messagebox.showwarning(title='File error', message='Data file not found')
        else:
            website = website_name_entry.get()
            if website in data_items:
                password = data_items[website]['password']
                email = data_items[website]['email']
                messagebox.showinfo(title='Search results', message=f"Website: {website}\n"
                                                                    f"Email: {email}\n"
                                                                    f"Password: {password}")
            else:
                messagebox.showerror(title='Website not found', message='Enter an existing website name or generate'
                                                                        ' new password instead')

    # ---------------------------- ADD PASSWORD UI SETUP ------------------------------- #
    # noinspection PyGlobalUndefined
    global password_bg, back_icon
    top = Toplevel()
    top.title("Password Manager")
    top.configure(padx=100, pady=40, bg='#fff')
    top.resizable(0, 0)

    def destroy_top():
        top.destroy()

    back_icon = ImageTk.PhotoImage(Image.open('back.png'))
    back_btn = Button(top, image=back_icon, bg='#fff', bd=0, command=destroy_top)
    back_btn.grid(column=0, row=0, sticky='NW')

    canvas = Canvas(top, height=200, width=200, highlightthickness=0)
    password_bg = PhotoImage(file="logo1.png")
    canvas.create_image(100, 100, image=password_bg)
    canvas.grid(column=1, row=0)

    website_name_label = Label(top, text='Website:', bg='#fff')
    website_name_label.grid(column=0, row=1, sticky='W')

    website_name_entry = Entry(top, bd=2, highlightthickness=0, relief='groove')
    website_name_entry.focus()
    website_name_entry.grid(column=1, columnspan=2, row=1, sticky='EW')

    user_info_label = Label(top, text="Email/Username:", bg='#fff')
    user_info_label.grid(column=0, row=2, pady=15, sticky='W')

    user_info_entry = Entry(top, bd=2, highlightthickness=0, relief='groove')
    user_info_entry.insert(0, 'user@gmail.com')
    user_info_entry.grid(column=1, columnspan=2, row=2, sticky='EW')

    password_label = Label(top, text="Password:", bg='#fff')
    password_label.grid(column=0, row=3, sticky='W')

    password_entry = Entry(top, bd=2, highlightthickness=0, relief='groove')
    password_entry.grid(column=1, row=3, sticky='EW')

    generate_password_btn = Button(top, text='Generate Password', relief='groove', command=generate_password)
    generate_password_btn.grid(column=2, row=3, pady=1, sticky='EW')

    add_btn = Button(top, text='Save', relief='groove', command=save_info)
    add_btn.grid(column=1, columnspan=2, row=4, sticky='EW', pady=10)

    search_btn = Button(top, text='search', command=find_password)
    search_btn.grid(column=1, row=5)


def open_window_two():
    global back_ico
    second = Toplevel()

    def destroy_top():
        second.destroy()

    back_ico = ImageTk.PhotoImage(Image.open('back.png'))
    back_btn = Button(second, image=back_ico, bg='#fff', bd=0, command=destroy_top)

    back_btn.grid(column=0, row=0, sticky='NW')
    search_label = Label(second, text='Search password')
    search_label.grid(column=0, row=1)


# ---------------------------- ROOT WINDOW UI SETUP ------------------------------- #
root = Tk()
root.title('Home Page')
root_icon = ImageTk.PhotoImage(Image.open('passicon.png'))
root.iconphoto(True, root_icon)
root.configure(padx=100, pady=100, bg='DeepPink4')

window1_btn = Button(root, text='Add Password', command=open_window_one, width=40)
window1_btn.grid(column=1, row=0)

window2_btn = Button(root, text='Retrieve Password', command=open_window_two, width=40)
window2_btn.grid(column=1, row=1, pady=10)

view_password_list = Button(root, text='View all passwords', width=40)
view_password_list.grid(column=1, row=2)
root.mainloop()
# TODO: prevent user from entering multiple website entries
