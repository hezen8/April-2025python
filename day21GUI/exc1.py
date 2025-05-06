from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Celsius to Fahrenheit Converter")
root.configure(bg="lightgreen")
root.geometry("500x500")

def convertToFahrenheit():
    celsius=float(txtCelsius.get())
    fahrenheit=(celsius-32)*5/9
    #fahrenheit=(celsius*9/5)+32
    #fahrenheit=(celsius*1.8)+32
    message=f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit"
    messagebox.showinfo("Celsius to Fahrenheit", message)

lblCelsius=Label(root,text=" Enter value in Degree Celsius:",bg="lightblue")
lblCelsius.pack()
txtCelsius=Entry(root,bg="pink")
txtCelsius.pack()

btnconverter=Button(root,text="Convert to Fahrenheit", command=convertToFahrenheit,bg="lightblue")
btnconverter.pack()


root.mainloop()