# TKINTER    INTERFACE INBUILT LIBRARY
# creating an interface that does not use commandline arguments
from tkinter import *

root = Tk()
root.title("First GUI")
# TO CHANGE THE SIZE OF THE WINDOW
root.geometry("500x500")
# to add a component to the window
lblMessage=Label(root,text="Welcome to python GUI programming",borderwidth=2,relief="solid",fg="grey",bg="yellow",font=("Italic",20,"bold"))
lblMessage.pack()

lblMessage2=Label(root,text=" Welcome to GUI Using the TKinter module")
lblMessage2.pack(ipadx=20,ipady=10,padx=20,pady=20,)

# to add a button to the window
txtName=Entry(root)
txtName.pack()

btnClickMe=Button(root,text="Click Here")
btnClickMe.pack()

#to make the window keep on running
root.mainloop()