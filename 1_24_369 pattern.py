n=int(input('Enter'))
for i in range(0,n):
    for j in range (0,i+1):
        print((i+1)*(j+1),end='')
    print()