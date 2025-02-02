email = input('Enter you email id')

username = email[:email.index('@')]
domain = email[email.index('@')+1:]

print ('your username is {} and domain is {}'.format(username,domain))