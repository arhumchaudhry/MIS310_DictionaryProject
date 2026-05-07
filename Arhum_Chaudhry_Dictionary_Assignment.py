# Part 1 - Understanding the dictionary
capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}
print(dir(capitals))
print(help(capitals))
print(capitals.get("Japan"))

# Part 2 - Checking for Keys
if capitals.get("Russia"):
    print("That capital exists")
else:
    print("That capital doesn't exist")
if capitals.get("India"):
    print("India exists")
else:
    print("India doesn't exist")
if capitals.get("Brazil"):
    print("Brazil exists")
else:
    print("Brazil doesn't exist")

# Part 3 - Updating the dictionary
capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.update({"France": "Paris"})
capitals.update({"Japan": "Tokyo"})
capitals.update({"Canada": "Ottawa"})
capitals.update({"USA": "Washington D.C."})
print(capitals)

# Part 4 - Removing Elements
capitals.pop("China")
capitals.popitem()
capitals.pop("Russia")
print(capitals)

# Part 5 - Print All Countries
for key in capitals.keys():
    print("Country:", key)
for value in capitals.values():
    print(value)
for key, value in capitals.items():
    print(key, "-", value)

# Part 6 - mini challenge
countries = {
    "USA": "Washington D.C.",
    "France": "Paris",
    "Japan": "Tokyo",
    "Canada": "Ottawa",
    "India": "New Delhi",
    "Brazil": "Brasilia"
}
country = input("Enter a country name: ")
capital = countries.get(country)
if capital:
    print("The capital of", country, "is", capital)
else:
    print("Country not found")
    answer = input("Would you like to add it? (yes/no): ")
    if answer == "yes":
        new_capital = input("Enter the capital city: ")
        countries[country] = new_capital
        print("Country added to dictionary")



