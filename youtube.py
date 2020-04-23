
import tkinter as tk

window = tk.Tk()
window.title("Youtube Videos Organizer")
window.geometry("400x400")

#LABELS
header = tk.Label(text="Organizing data from trending videos")
header.grid(column=0, row=0)

create_user = tk.Label(text= "Create Username for account")
create_user.grid(column= 0, row=1)

create_password = tk.Label(text= "Create password for account")
create_password.grid(column=0, row=2)

create_email = tk.Label(text="Enter email address")
create_email.grid(column=0, row=3)

create_phonenum = tk.Label(text="Enter your phone number")
create_phonenum.grid(column=0, row=4)

login = tk.Label(text="Enter login if you already created an account")
login.grid(column=0, row=5)

#ENTRIES
entry1 = tk.Entry()
entry1.grid(column=1, row=1)


entry2 = tk.Entry()
entry2.grid(column=1, row=2)

entry3 = tk.Entry()
entry3.grid(column=1, row=2)

entry4 = tk.Entry()
entry4.grid(column=1, row=4)

entry5 = tk.Entry()
entry5.grid(column=1, row=5)


#BUTTON
button1 = tk.Button()
button1.grid(column=0, row=2)

button2 = tk.Button()
button2.grid(column=0, row=3)

button3 = tk.Button()
button3.grid(column=0, row=4)

button4 = tk.Button()
button4.grid(column=0, row=5)

button5 = tk.Button()
button5.grid(column=0, row=6)




window.mainloop()