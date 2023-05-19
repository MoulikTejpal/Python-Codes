n=int(input('Enter the no. of elements'))
l=[]
sum1=0
print('Enter the list of elements')
for i in range(n):
    x=int(input())
    l.append(x)
for i in l:
    sum1=sum1+i
print(sum1)