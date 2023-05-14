n=int(input('Enter the no. of elements'))
l=[]
l_new=[]
print('Enter the list of elements')
for i in range(n):
    x=int(input())
    l.append(x)
for i in l:
    a=l.count(i)
    if a%2==1 and i not in l_new:
        l_new.append(i)
print(l_new)