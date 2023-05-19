def fib(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return (fib(x-1) + fib(x-2))
 
terms=int(input('Enter no. of terms'))
for i in range(0, terms):
    print(fib(i))