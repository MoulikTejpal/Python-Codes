x=input('Enter a string: ')
y=input('Enter the sub-string: ')
if y in x:
    print(x.count(y))
    z=x.split(' ')
    for i in z:
        if i==y:
            z.remove(i)
    print(' '.join(z))
else:
    print('Sub-string not found in string')