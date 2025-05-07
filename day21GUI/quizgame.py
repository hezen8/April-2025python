
from random import randint
from tkinter import*
from tkinter import messagebox


countries= ["Algeria","Angola","Benin","Botswana","Burundi","Burkina Faso","Cameroon",
"Cape Verde","Central African Republic","Chad","Comoros","Cote d’Ivoire","DR Congo","Djibouti",
"Egypt","Equatorial Guinea","Eritrea","Ethiopia","Gabon","Gambia","Ghana","Guinea",
"Guinea-Bissau","Kenya","Lesotho","Liberia","Libya","Madagascar","Malawi","Mali","Mauritania",
"Mauritius","Morocco","Mozambique","Namibia","Niger","Nigeria","Republic of the Congo","Réunion",
"Rwanda","São Tomé and Principe","Senegal","Seychelles","Sierra Leone","Somalia","South Africa","South Sudan",
"Sudan","Swaziland","Tanzania","Togo","Tunisia","Uganda","Zambia","Zimbabwe"]

cities= ["Algiers","Luanda","Porto-Novo","Gaborone","Bujumbura","Ouagadougou","Yaoundé","Praia","Bangui","N’Djamena","Moroni","Yamoussoukro","Kinshasa","Djibouti City",
        "Cairo","Malabo","Asmara", "Addis Ababa","Libreville","Banjul","Accra","Conakry","Bissau","Nairobi","Maseru","Monrovia","Tripoli","Antananarivo","Lilongwe","Bamako","Nouakchott", "Port Louis","Rabat","Maputo","Windhoek","Niamey", "Abuja","Brazzaville","Saint-Denis",
        "Kigali","São Tomé","Dakar","Victoria","Freetown","Mogadishu","Pretoria","Juba",
        "Khartoum","Mbabane","Dodoma","Lome","Tunis","Kampala","Lusaka","Harare"]


# qn="What is the capital city of"
# point=0
# rand= randint(0,len(countries)-1)
# print(qn + ""+countries[rand])
# ans=input()
#     # if ans.upper()==cities[rand].upper:
#     #     print("correct")
#     #     point+=1
#     # else:
#     #     print("Incorrect")
#     #     print(f"{cities[rand]} is the correct answer")
#     #     print(f"{point}")
        
# if ans.upper()==cities[rand].upper():
#     print("correct")
#     point+=1
# else:
#     print("Incorrect")
#     print(f"{cities[rand]} is the correct answer")


# print(f"you scored {point} out of {len(qn)}")



root=Tk()
correctAnswer=StringVar()
def generatequiz():
    qn="What is the capital city of"
    rand= randint(0,len(countries)-1)
    qn=qn +" " +countries[rand]
    c_ans= cities[rand]
    correctAnswer.set(c_ans)
    question.set(qn)
    

    
root.config(bg="indigo")
root.geometry("400x200")
root.title("Quiz Game")
question=StringVar()


lblQuestion=Label(root,textvariable=question)
lblQuestion.grid(row=0,column=0)

lblanswer=Label(root,text="Enter your answer")
lblanswer.grid(row=1,column=0)
txtanswer=Entry(root)
txtanswer.grid(row=1,column=1,pady=10)

btnquizes=Button(root,text="Another Quiz",command=generatequiz)
btnquizes.grid(row=2,column=0)

def checkAns():
    
    ans=txtanswer.get()
    if ans.upper().strip()==correctAnswer.get().upper():
        messagebox.showinfo("Result","Correct")
    else:
        messagebox.showinfo("Result",f"Incorrect +{correctAnswer.get()} is the correct answer")


btnanswer=Button(root,text="Check Answer",command=checkAns)
btnanswer.grid(row=2,column=1,pady=10)

btnquit=Button(root,text="Quit",command=root.quit)
btnquit.grid(row=2,column=2)

root.mainloop()


