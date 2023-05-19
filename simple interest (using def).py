def si(p=0,r=5,t=1):
    interest=(p*r*t)/100
    return(interest)
x=float(input())
y=float(input())
z=float(input())
print(si(x,y,z))
print(si(x,y))
print(si(x))