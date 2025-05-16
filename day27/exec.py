#using python to acces sqlite database
#orm Object relational mapper
#formatted string(f"")
#formats your text
#adding a scrollbar
import sqlite3
from tkinter import*
from tkinter import messagebox

root=Tk()
root.title("My Database")
root.geometry("500x500")
root.configure(bg="lightgreen")
conn=sqlite3.connect("books.db")
c=conn.cursor()

def addBook():
    conn=sqlite3.connect("books.db")
    c=conn.cursor()
    queryString=f"INSERT INTO books (\'{txtBookPrice.get()}\',\'{txtBookTitle.get()}\')"
    c.execute(queryString)
    conn.commit()
    conn.close()

    #leaving a blank on the interface after entering data and submitted
    txtBookTitle.delete(0,END)
    txtBookPrice.delete(0,END)
  
def showBooks():
    conn=sqlite3.connect("books.db")
    c=conn.cursor()
    queryString="SELECT *,rowid FROM books"
    c.execute(queryString)
    records = c.fetchall()
    displayBooks=""

    for record in records:
        displayBooks+=str(record[0]) +" "+str(record[1])+" "+str(record[2]) +"\n"
        #displaying the record
    lblShowBooks=Label(root,text=displayBooks,justify="left")
    lblShowBooks.grid(row=10,column=0,columnspan=2,ipadx=10,pady=10)

def DeleteBook():
    conn=sqlite3.connect("books.db")
    c=conn.cursor()
    queryString="DELETE FROM books WHERE rowid="+txtBookId.get()
    c.execute(queryString)
    conn.commit()
    conn.close()
#we ned to create a new window
def UpdateBook():
    updatewin=Tk()
    updatewin.title("Update Books")
    updatewin.geometry("500x500")
    updatewin.config(bg="skyblue")
    bookID=txtBookId.get()
    conn=sqlite3.connect("books.db")
    c=conn.cursor()
    queryString="SELECT * FROM books WHERE rowid="+txtBookId.get()
    c.execute(queryString)
    records=c.fetchall()

    lblTitleUpdate=Label(updatewin,text="UPDATE BOOK",bg="grey")   
    lblBookTitleUpdate=Label(updatewin,text="Update Book Title",bg="grey")
    txtBookTitleUpdate=Entry(updatewin,width=50)
    lblTitleUpdate.grid(row=0,column=0,columnspan=2)
    lblBookTitleUpdate.grid(row=1,column=0,pady=10,padx=10)
    txtBookTitleUpdate.grid(row=1,column=1,pady=10)

    lblBookPriceUpdate=Label(updatewin,text="Book Price",bg="grey")
    txtBookPriceUpdate=Entry(updatewin,width=50)
    lblBookPriceUpdate.grid(row=2,column=0,pady=10)
    txtBookPriceUpdate.grid(row=2,column=1,pady=10)

    for record in records:
        txtBookTitleUpdate.insert(0,record[0])
        txtBookPriceUpdate.insert(0,record[1])

    def saveChanges():
        conn=sqlite3.connect("books.db")
        c=conn.cursor()

        btitle=txtBookTitleUpdate.get()
        bprice=txtBookPriceUpdate.get()
        
        c.execute("""UPDATE books SET
        BookTitle=?, BookPrice=?
        WHERE rowid=oid""", (btitle,bprice))
        conn.commit()
        conn.close()

    btnUpdateBook=Button(updatewin,text="Save changes",command=saveChanges)
    btnUpdateBook.grid(row=3,column=0,columnspan=2,ipadx=10,pady=10)

    conn.commit()
    conn.close()


lblTitle=Label(root,text="BOOKS LIBRARY",bg="lightblue")   
lblBookTitle=Label(root,text="Book Title",bg="lightblue")
txtBookTitle=Entry(root,width=50)
lblTitle.grid(row=0,column=0,columnspan=2)
lblBookTitle.grid(row=1,column=0,pady=10)
txtBookTitle.grid(row=1,column=1,pady=10)

lblBookPrice=Label(root,text="Book Price",bg="lightblue")
txtBookPrice=Entry(root,width=50)
lblBookPrice.grid(row=2,column=0,pady=10)
txtBookPrice.grid(row=2,column=1,pady=10)

lblBookId=Label(root,text="Enter Book Id",bg="Lightblue")
lblBookId.grid(row=7,column=0,ipadx=10,pady=10)

txtBookId=Entry(root,text="Enter Book Id",)
txtBookId.grid(row=7,column=1,ipadx=10,pady=10)

btnDeleteRecord=Button(root,text="Delete Record",command=DeleteBook,bg="magenta")
btnDeleteRecord.grid(row=8,column=0,columnspan=2,ipadx=10,pady=10)

btnShowBooks=Button(root,text="Show Books",command=showBooks,bg="magenta")
btnShowBooks.grid(row=6,column=0,columnspan=2,ipadx=100,pady=0)

#fusing pythton with sql
btnAddRecord=Button(root,text="Add new Book",command=addBook,bg="magenta")
btnAddRecord.grid(row=4,column=0,columnspan=2, ipadx=100)

btnUpdateBook=Button(root,text="Update Book",command=UpdateBook,bg="magenta")
btnUpdateBook.grid(row=9,column=0,columnspan=2,ipadx=100,pady=10)

conn.commit()
conn.close()
root.mainloop()