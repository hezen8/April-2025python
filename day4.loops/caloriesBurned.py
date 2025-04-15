RATE=4.2

counter=10
for counter in range(10,40,5):
    calories=float(input("Enter number of calories to be burned"))
    burned_calory= calories % RATE
    counter=counter+5

print(f"number of calories burned after-{counter} is-{burned_calory}")
