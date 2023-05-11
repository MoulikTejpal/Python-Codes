x=input('Enter')
y=x.lower()
list=[]
for m in y:
    if m=='a' or m=='e' or m=='i' or m=='o' or m=='u':
        list.append(m)
print('The no. of vowels = ',len(list))