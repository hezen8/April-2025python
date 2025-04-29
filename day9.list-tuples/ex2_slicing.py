#slicing
eastafricaCountries=["Kenya","Uganda","Tanzania","Somalia","Rwanda","Burundi","Kenya"]
print(eastafricaCountries[0:3])
print(eastafricaCountries[2:6])
print(eastafricaCountries[:-2])
print(eastafricaCountries[2:])

#sorting
copyCountries=eastafricaCountries.copy()
copyCountries.sort(reverse=True)
print(copyCountries)
print(sorted(eastafricaCountries))
print(eastafricaCountries.count("Kenya"))