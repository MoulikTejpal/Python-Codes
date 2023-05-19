x=input()
y=list(x)
reverse=[]
for i in y[-1::-1]:
    reverse.append(i)
if y==reverse:
    print('palindrome string')
else:
    print('normal string')