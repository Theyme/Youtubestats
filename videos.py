import tkinter as tk 


def Registration():






 
    """page2text.pack_forget()
    page1text.pack()  
    
    create_user = Label(window, text="Username").grid(row=0)
    create_password = Label(window, text="Password").grid(row=1) 
    create_email = Label(window, text="E-mail Address").grid(row=2)
    create_phonenum = Label(window, text="Phone Number").grid(row=3)
                                     
           
e1 = Entry(window) 
e2 = Entry(window)
e3 = Entry(window)
e4 = Entry(window)

e1.grid(row=0, column=1) 
e2.grid(row=1, column=1)                                   
e3.grid(row=1, column=1)
e4.grid(row=1, column=1)
"""
def Login():
    page1text.pack_forget()
    page2text.pack()
    
                                           
    

window = tk.Tk()


page1btn = tk.Button(window, text="Page 1", command=Registration)       
page2btn = tk.Button(window, text="Page 2", command=Login)       

page1text= tk.Label(window, text="Registration Page")             
page2text = tk.Label(window, text="Login Page")             

page1btn.pack()                                                
page2btn.pack()                                                                             
page1text.pack()                                                


window.mainloop() 
