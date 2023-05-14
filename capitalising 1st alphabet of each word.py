x=input()
list1=x.split()
list2=[]
for i in list1:
    list2.append(i.capitalize())
print(' '.join(list2))