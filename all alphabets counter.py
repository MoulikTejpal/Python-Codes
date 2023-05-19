x=input('Enter')
y=x.lower()
list1=[]
dictionary={}
for i in y:
    count=0
    if i not in list1:
        list1.append(i)
        for m in y:
            if m==i:
                count=count+1
        dictionary[i]=count
print(dictionary)