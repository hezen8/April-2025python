movierating=input("Enter nameof the movies")
total=0
for counter in range(0,4):
    while movierating<0 or movierating>4:
        print("Enter a valid rating (<0 or >4)")
    movierating=total+movierating
    average=movierating/4
print(f"average star rating of the movie is -{average}stars")