name = input("Enter the name to print the Acronym ")
text = name.split()

acronym = ' '

for item in text:
     acronym = acronym + item[0].upper()

print(acronym)