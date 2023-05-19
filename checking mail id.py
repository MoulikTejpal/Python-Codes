import re
x=input('Enter mail id: ')
if re.match('([a-zA-Z][a-zA-Z0-9_\.]*[a-zA-Z0-9])@([a-zA-Z][a-zA-Z0-9]*)\.([a-zA-Z]*)',x):
    print('Valid')
else:
    print('Not Valid')