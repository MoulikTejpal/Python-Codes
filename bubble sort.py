n=int(input('Enter the no. of elements'))
l=[]
print('Enter the list of elements')
for x in range(n):
    a=int(input())
    l.append(a)
for i in range(n):
    for j in range(0,n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
        print(l)