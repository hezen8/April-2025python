rooms={
"CS101":"3004",
"CS102":"4501",
"CS103":"6755",
"NT110":"1244",
"CM241":"1411"
}

instructors={
"CS101":"Haynes",
"CS102":"Alvarado",
"CS103":"Rich",
"NT110":"Burke",
"CM241":"Lee"
}

meetingTime={
"CS101":"8:00.am",
"CS102":"9:00.am",
"CS103":"10:00.am",
"NT110":"11:00.am",
"CM241":"1:00.pm"
}
courseNo=input("Please enter the course number you wish to search")

if courseNo not in rooms.keys():
    print("course not found")
else:
    print(f"Room No: {rooms[courseNo]}")
    print(f"Instructor:{instructors[courseNo]}")
    print(f"Meeting time:{meetingTime[courseNo]}")
    
