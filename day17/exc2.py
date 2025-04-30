def get_menuchoice():
    print()
    print("My Addres book")
    print("*************")
    print("1-search for a contact")
    print("2-add a contact")
    print("3-update a contact")
    print("4-delete a contact")
    print("5-quit the program")

    choice=int(input("Enter your choice"))

    while choice<1 or choice>5:
        choice=int(input("Enter a valid choice(1-5)"))

    return choice

def search(contacts):
    name=input("Enter name of contact to search")
    print(contacts.get(name,"not found"))

def add(contacts):
    name=input("Enter name")
    phone=input("Enter phone number")
    email=input("Enter an email")
    try:
        len(phone)<10
        print("PHONE NUMBER IS INCOMPLETE")
    except:
        print("proceed")
    if name not in contacts:
        contacts[name]={"Tel":phone,"email":email}
        print("contact added successfully")
    else:
        print("Contact alredy exists")

def update(contacts):
    name=input("Enter name to update")
    email=input("Enter email to update")
    if name in contacts:
        phone=input("Enter new phone number to update")
        email=input("Enter new email to update")
        contacts[name]["Tel"]=phone
        contacts[name]["email"]=email
        print("Contact updated successfully")
    else:
        print("Name not found/doesn,t exist")

def delete(contacts):
    name=input("Enter name to delete(remove)")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully")
    else:
        print("Name not found/doesn,t exist")

def main():
    contacts={}
    choice=0
    while choice !=5:
        choice = get_menuchoice()
        if choice ==1:
            search(contacts)
        elif choice==2:
            add(contacts)
        elif choice==3:
            update(contacts)
        elif choice==4:
            delete(contacts)

main()