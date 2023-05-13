n=int(input('Enter any no.'))
r=n
sum1=0
while r>0:
    x=r%10
    sum1=sum1+x**3
    r=r//10
if sum1==n:
    print("Armstrong no.")
else:
    print("Not Armstrong no.")