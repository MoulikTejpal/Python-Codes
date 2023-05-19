t1=('sub1','sub2','sub3')
t2=('sub2', 'sub4','sub5')
t3=('sub1','sub4','sub6')
T=t1+t2+t3
l=[]
for i in T:
    if i not in l:
        l.append(i)
print(tuple(l))