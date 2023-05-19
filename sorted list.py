n=int(input('Enter the no. of elements'))
l=[]
print('Enter the list of elements')
for i in range(n):
    x=int(input())
    l.append(x)
l_new=l
l_new.sort()
if l==l_new:
    print('Ascending Order')
else:
    print('Not sorted')