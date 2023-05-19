n=int(input('Enter the no. of elements'))
l=[]
print('Enter the list of elements')
for i in range(n):
    x=int(input())
    l.append(x)
a=l[1]
for i in l:
    if i>a:
        a=i
print('The maximum is',a)