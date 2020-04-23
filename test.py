
import tkinter as tk 


def Registration():
    page2text.pack_forget()
    page1text.pack()                                    
                                              

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




"""
import tkinter as tk 

def Welcome():


def Registration():
    page2text.pack_forget()                                     #logintext.pack_forget()
    page1text.pack()                                            #registrationtext.pack_forget()

def Login():
    page1text.pack_forget()                                     #registrationtext.pack_forget()
    page2text.pack()                                            #logintext.pack_forget()
    

window = tk.Tk()

page1btn = tk.Button(window, text="Page 1", command=page1)       #regbtn
page2btn = tk.Button(window, text="Page 2", command=page2)       #loginbtn

page1text = tk.Label(window, text="This is page 1")             #registrationtext.pack_forget()
page2text = tk.Label(window, text="This is page 2")             #logintext.pack_forget()

page1btn.pack()                                                 #regbtn.pack()
page2btn.pack()                                                 #loginbtn.pack()                             
page1text.pack()                                                #registrationtext.pack_forget()

window.mainloop() 
"""