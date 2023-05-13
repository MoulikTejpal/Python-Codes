n=int(input('Enter'))
x=1
for i in range(0,n):
    for j in range (0,i+1):
        print(x,end='')
        x=x+1
    print()