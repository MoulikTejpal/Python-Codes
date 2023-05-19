a1=int(input('Enter no. of elements in set 1'))
b1=int(input('Enter no. of elements in set 2'))
c1=int(input('Enter no. of elements in set 3'))
a=set()
b=set()
c=set()
for i in range(a1):
    a.add(int(input('Enter element for set 1')))
for i in range(b1):
    b.add(int(input('Enter element for set 2')))
for i in range(c1):
    c.add(int(input('Enter element for set 3')))
common=a&b&c
if common==set():
    print('No common elements')
else:
    print(common)