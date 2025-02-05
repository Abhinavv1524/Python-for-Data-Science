def convert(f):
    fer = float(f)
    c = (f-32)*5/9

    return c

ferh = float(input("Enter the temp in F"))

cels = convert(ferh)

print("The temprature in Celsius is ",cels)