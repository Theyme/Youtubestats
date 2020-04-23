
from tkinter import *
import os

# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global email
    global phonenumber
    global username_entry
    global password_entry
    global email_entry
    global phonenumber_entry
    
    username = StringVar()
    password = StringVar()
    email = StringVar()
    phonenumber = StringVar()
    

    Label(register_screen, text="Please enter details below", bg="red").pack()
    Label(register_screen, text="").pack()
    
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    
    
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    
    email_lable = Label(register_screen, text="Email Address * ")
    email_lable.pack()
    
    
    email_entry = Entry(register_screen, textvariable=email)
    email_entry.pack()
    
    
    phonenumber_lable = Label(register_screen, text="Phone Number * ")
    phonenumber_lable.pack()
    
    phonenumber_entry = Entry(register_screen, textvariable=phonenumber)
    phonenumber_entry.pack()
    
    
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue").pack()

# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="YOUTUBE VIDEO ORGANIZER", bg="red", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30").pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()