m=int(input())
n=int(input())
mat1=[]
for i in range(m):
    l=[]
    for j in range(n):
        l.append(int(input()))
    mat1.append(l)
print(mat1)
mat2=[]
for i in range(m):
    l=[]
    for j in range(n):
        l.append(int(input()))
    mat2.append(l)
print(mat2)
sum_mat=[]
for i in range(m):
    l=[]
    for j in range(n):
        l.append(0)
    sum_mat.append(l)
for i in range(len(mat1)):            #can use range(m)
    for j in range(len(mat1[i])):     #can use range(n)
        sum_mat[i][j]=mat1[i][j]+mat2[i][j]
for row in sum_mat:
    print(row)