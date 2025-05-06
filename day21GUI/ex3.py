from tkinter import *
from tkinter import messagebox
def displayMessage():
    messagebox.showinfo("Information", "Welcome to Python GUI Programming")

root=Tk()

root.geometry("500x500")

btnsubmit=Button(root,text="Click Here", command=displayMessage)
btnsubmit.pack()

#to add a quit button to the GUI
btnquit=Button(root,text="Quit", command=root.quit)#Or root.Destroy
btnquit.pack()

root.mainloop()
