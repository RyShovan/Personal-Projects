"""
Version 2.0
Script Concept by Pritam.
"Let's write a program to access name starts with specific
letter/letters from a name database."
"""

name_list = ["Anari", "kamal", "Bahana", "Ana", "Partha"]

# name_get = []
def name_search(name):
    name_get = []
    for i in name_list:
        if name.lower() in i.lower():
            if len(name) == 1:
                if name[0].lower() == i[0].lower():
                    name_get.append(i)
            elif len(name) == 2:
                if name[0:2].lower() == i[0:2].lower():
                    name_get.append(i)
            elif len(name) == 3:
                if name[0:3].lower() == i[0:3].lower():
                    name_get.append(i)
            elif len(name) == 4:
                if name[0:4].lower() == i[0:4].lower():
                    name_get.append(i)
            else:
                name_get.append(i)
    return name_get

name_input = input("Enter the name: ")

name_get = name_search(name_input)

print(name_get)
