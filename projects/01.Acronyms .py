name = input("Enter the name to print the Acronym ")
text = name.split()
a = ' '

for i in text:
     a = a + i[0].upper()

print(a)