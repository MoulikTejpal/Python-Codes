n=int(input('Enter the no. of elements'))
l=[]
print('Enter the list of elements')
for i in range(n):
    x=int(input())
    l.append(x)
a=input('Enter the element to check for')
x=0
for i in l:
    if i==a:
        x=x+1
if x>0:
    print('The element exists in the list',x,'times')
else:
    print('Element not found')