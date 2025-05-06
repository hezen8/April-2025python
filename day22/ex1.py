from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("miles-per-gallon converter")
root.geometry("500x500")
root.configure(bg="lightgreen")

def calaculateMPG():

    gallons=float(txtgallons.get())
    miles=float(txtmiles.get())
    mpg=miles/gallons
    message=f"{gallons} gallons of gas can drive {miles} miles at {mpg} miles per gallon"
    messagebox.showinfo("miles-per-gallon", message)


lblgallons=Label(root,text="Enter number of gallons of gas the car holds:",bg="magenta",font=("Italic", 10))
lblgallons.pack()
txtgallons=Entry(root)
txtgallons.pack()

lblmiles=Label(root,text="Enter number of miles it can be driven on a full Tank:",bg="magenta",font=("Italic", 10))
lblmiles.pack()
txtmiles=Entry(root)
txtmiles.pack()

btncalcMpG=Button(root,text="calculate Mpg",command=calaculateMPG,bg="magenta",font=("Italic", 10))
btncalcMpG.pack()

btnquit=Button(root,text="Quit",command=root.quit,bg="magenta",font=("Italic", 10))
btnquit.pack()

root.mainloop()