import sqlite3
from tkinter import*


root=Tk()
root.configure(bg="lightgreen")
root.geometry("500x500")
root.title("WEBSITE")
conn=sqlite3.connect("users.db")
c=conn.cursor()

def Logging():
    conn=sqlite3.connect("users.db")
    c=conn.cursor()
    username=txtUsername.get()
    password=txtpass.get()
    queryString="""SELECT * FROM tblusers WHERE username=? AND password=?"""
    c.execute(queryString,(username,password))
    conn.commit()
    conn.close()

lblLogin=Label(root,text="Enter your name")
lblLoginpass=Label(root,text="Enter Password")
lblLogin.grid(row=1,column=0,ipadx=10,pady=10)
lblLoginpass.grid(row=2,column=0,ipadx=10,pady=10)
txtUsername=Entry()
txtpass=Entry()
txtUsername.grid(row=1,column=1,ipady=10,padx=10)
txtpass.grid(row=2,column=1,ipady=10,padx=10)


btnLogin=Button(root,text="Log In",command=Logging,bg="Magenta")
btnLogin.grid(row=3,column=0,columnspan=2)




conn.commit()
conn.close()
root.mainloop()