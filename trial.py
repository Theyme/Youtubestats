import tkinter as tk
from functools import partial

'''def register( create_user, create_password, create_email, create_phonenum):

    print("username entered :", create_user.get())
    print("password entered :", create_password.get())
    print("Email entered :", create_email.get())
    print("Phone number entered :", create_phonenum.get())
    return
    '''
       


#window
window = tk.Tk()
window.geometry('400x150')  
window.title('Youtube video Organizer')

#username label and text entry box
create_userLabel = Label(window, text="User Name").grid(row=0, column=0)
create_user = StringVar()
create_userEntry = Entry(window, textvariable=create_user).grid(row=0, column=1) 

#Password label and text entry box
create_passwordLabel = Label(window, text="Password").grid(row=1, column=0)
create_password = StringVar()
create_passwordEntry = Entry(window, textvariable=create_password).grid(row=1, column=1) 

#Email label and text entry box
create_emailLabel = Label(window, text="Email Address").grid(row=1, column=0)
create_email = StringVar()
create_emailEntry = Entry(window, textvariable=create_email).grid(row=1, column=1) 

#Phone number label and text entry box
create_phonenumLabel = Label(window, text="Phone Number").grid(row=1, column=0)
create_phonenum = StringVar()
create_phonenumEntry = Entry(window, textvariable=create_phonenum).grid(row=1, column=1) 


register = partial(register, create_user, create_password, create_email, create_phonenum)  


#login button
loginButton = Button(window, text="Login", command=register).grid(row=4, column=0)  


window.mainloop()