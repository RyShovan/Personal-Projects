"""
Script Concept by Pritam.
"Let's write a program to access name starts with specific
letter/letters from a name database."

This is version 1.0 of the script.
Issues: If I give input "Ana" it includes "Bahana" in results.
It should have printed only "Anari" and "Ana".
In version 2.0 I will solve this bug.
"""

name_list = ["Anari", "kamal", "Bahana", "Ana", "Partha"]

# name_get = []
def name_search(name):
    name_get = []
    for i in name_list:
        if name.lower() in i.lower():
            name_get.append(i)
    return name_get

name_input = input("Enter the name: ")

name_get = name_search(name_input)

print(name_get)
