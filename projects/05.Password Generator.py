import random
length = int(input('Enter the length of password '))
password = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

pas = "".join(random.sample(password,length))

print(pas)