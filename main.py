from random import shuffle
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8,10)
    nr_numbers = random.randint(2,4)
    nr_symbols = random.randint(2,4)
    password_letters = [random.choice(letters) for nr in range(nr_letters)]
    password_numbers = [random.choice(numbers) for nr in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for nr in range(nr_symbols)]
    password_generated_list = [item for sublist in [password_letters,password_numbers,password_symbols] for item in sublist]
    shuffle(password_generated_list)
    password_generated = ''.join(password_generated_list)
    pwd_entry.delete(0,END)
    pwd_entry.insert(0,password_generated)
    pyperclip.copy(password_generated)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = url.get()
    mail = email.get()
    password = pwd.get()
    new_data = {
        website: {
            "email": mail,
            "password": password
        }
    }

    empty_verification = verify_emptyfields(website,mail,password)

    if empty_verification:
        try:
            with open("./data.json",'r') as file:
                file_l = json.load(file)
        except FileNotFoundError:
            print("File created")
            with open("./data.json", "w") as data_json:
                json.dump(new_data, data_json, indent=4)
        else:
            file_l.update(new_data)
            with open("./data.json", "w") as updating:
                json.dump(file_l, updating, indent=4)
        finally:
            website_entry.delete(0,END)
            email_entry.delete(0, END)
            pwd_entry.delete(0, END)
            website_entry.focus()
    else:
        website_entry.focus()

def verify_emptyfields(website,mail,password):
    data_to_verify = [website,mail,password]
    for _ in data_to_verify:
        if _ == '':
            messagebox.showwarning(title='Oops',message="Please don't leave fields empty")
            return False
        else:
            return True
def search_website():
    website = url.get()
    print('Searching... website')
    with open("./data.json",'r') as file:
        data = json.load(file)
        if website in data:
            username=data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website,message=f"{username}\n{password}")
        else:
            print(f"Website {website} does not exist")


# ---------------------------- UI SETUP ------------------------------- #


pwd_window = Tk()
pwd_window.configure(padx=50,pady=50)
pwd_window.title('Password Manager')

#Background
bk_image = PhotoImage(file='./logo.png')
canvas_pwd = Canvas(width=200,height=200)
canvas_pwd.create_image(100,100,image=bk_image)
canvas_pwd.grid(column=1,row=0)

#Labels
website_label = Label(text='Website:')
email_label = Label(text='Email/Username:')
password_label = Label(text='Password:')
website_label.grid(column=0,row=1)
email_label.grid(column=0,row=2)
password_label.grid(column=0,row=3)

#Input text Entries
url = StringVar()
pwd = StringVar()
email = StringVar()
website_entry = Entry(pwd_window,textvariable=url,font=('calibre',10),width=36,justify='left')
email_entry = Entry(pwd_window,textvariable=email,font=('calibre',10),justify='left', width=36)
pwd_entry = Entry(pwd_window,textvariable=pwd,font=('calibre',10),width=25)
website_entry.grid(column=1,columnspan=2,row=1,sticky='w')
website_entry.focus()
email_entry.grid(column=1,columnspan=2,row=2,sticky='w')
email_entry.insert(0,'example@domain.com')
pwd_entry.grid(column=1,row=3,sticky='w')

#Buttons
generate_button = Button(text='Generate Password',font=('calibre',10),command=generate_password)
add_button = Button(text='Add',font=('calibre',10),command=add_password,width=31,justify='left')
search_button = Button(text='Search',font=('calibre',10),command=search_website)
generate_button.grid(column=2,row=3,sticky='w')
add_button.grid(column=1,row=4,columnspan=2,sticky='w')
search_button.grid(column=2,row=1,sticky='e')
pwd_window.mainloop()



