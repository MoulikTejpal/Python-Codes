n=int(input('Enter the no. of elements'))
l_even=[]
l_odd=[]
print('Enter the list of elements')
for i in range(n):
    x=int(input())
    if x%2==0:
        l_even.append(x)
    else:
        l_odd.append(x)
print(l_even)
print(l_odd)