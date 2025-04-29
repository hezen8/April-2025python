with open("employees.txt") as f:
    # contents=f.read()
# print(contents)
#or
    # for line in f:
    #     print(line)

     for line in f:
        print(line.strip())