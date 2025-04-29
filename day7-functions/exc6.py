def calc_average(test1,test2,test3,test4,test5):
    return (test1+test2+test3+test4+test5)/5

def determine_grade(test):
    if (test<0 or test>100):
        print("Error not a valid")
        print("\n")
    elif test>=90:
        return "A"
    elif test>=80:
        return "B"
    elif test>=70:
        return "C"
    elif test>=60:
        return "D"
    else:
        return "F"
def main():
    test1=int(input("Enter Test1 scores"))
    test2=int(input("Enter Test2 scores"))
    test3=int(input("Enter Test3 scores"))
    test4=int(input("Enter Test4 scores"))
    test5=int(input("Enter Test5 scores"))

    print(f"Grade for test1 is {determine_grade(test1)}")
    print(f"Grade for test2 is {determine_grade(test2)}")
    print(f"Grade for test3 is {determine_grade(test3)}")
    print(f"Grade for test4 is {determine_grade(test4)}")
    print(f"Grade for test5 is {determine_grade(test5)}")

    average=calc_average(test1,test2,test3,test4,test5)
    print(f"The average score is {average}")

main()