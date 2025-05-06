from tkinter import *
from tkinter import messagebox

root=Tk()

root.title("Rectangle Area")
root.geometry("500x500")



def getArea():
        
    Length=float(txtlength.get())
    Width=float(txtwidth.get())
    Area=Length*Width
    message=f"the Area is{Area} sq units"
    messagebox.showinfo("Rectangle Area", message)

lblwidth=Label(root,text="Enter Width:")
lblwidth.pack()
txtwidth=Entry(root)
txtwidth.pack()

lbllength=Label(root,text="Enter Length:")
lbllength.pack()
txtlength=Entry(root)
txtlength.pack()

btncalaculateArea=Button(root,text="calculateArea", command=getArea)
btncalaculateArea.pack()

    #to add a quit button to the GUI
btnquit=Button(root,text="Quit", command=root.quit)#Or root.Destroy
btnquit.pack()

root.mainloop()