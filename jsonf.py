# Get input
names_input = input("List of names are: ")

names_list = names_input.split()
capitalized_names = [name.capitalize() for name in names_list]

for name in capitalized_names:
    print(name)
