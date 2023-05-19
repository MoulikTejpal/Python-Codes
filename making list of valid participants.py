import re
participants={}
for i in range(int(input('No. of enteries:'))):
    x=input('Enter reg no.: ')
    if re.match('([01][0-9]|[2][01])[a-zA-Z]{3}[0-9]{4}$',x): # $ is for ending
        participants[input('Name: ')]=x
print('Valid paarticipants: ',participants)