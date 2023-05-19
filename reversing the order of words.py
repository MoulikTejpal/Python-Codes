x=input()
list1=x.split(' ')
list2=[]
for i in list1[-1::-1]:
    list2.append(i)
ans=' '.join(list2)
print(ans)