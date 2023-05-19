n=int(input('Enter the no. of elements'))
l=[]
print('Enter the list of elements')
for i in range(n):
    x=int(input())
    l.append(x)
for i in l:
    if i%2==0:
        print(i)