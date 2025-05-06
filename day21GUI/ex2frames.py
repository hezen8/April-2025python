# using frames to organize the layout of the window
from tkinter import *

root = Tk()
root.title("First GUI")
# TO CHANGE THE SIZE OF THE WINDOW
root.geometry("500x500")

topFrame=Frame(root)
bottomFrame=Frame(root)

# to add a component to the window
lblMessage=Label(topFrame,text="Welcome to python GUI programming",borderwidth=2,relief="solid",fg="grey",bg="yellow",font=("Italic",20,"bold"))
lblMessage.pack()

lblMessage2=Label(topFrame,text=" Welcome to GUI Using the TKinter module")
lblMessage2.pack(ipadx=20,ipady=10,padx=20,pady=20)

# to add a button to the window
txtName=Entry(bottomFrame)
txtName.pack()

btnClickMe=Button(bottomFrame,text="Click Here")
btnClickMe.pack()

topFrame.pack(side="top")
bottomFrame.pack(side="top")

chkTickme=Checkbutton(bottomFrame,text="on/off")
chkTickme.pack()

#to make the window keep on running
root.mainloop()