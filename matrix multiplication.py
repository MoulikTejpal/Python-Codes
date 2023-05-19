m=int(input('Enter no. of rows'))
n=int(input('Enter no. of columns'))
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
product=[]
for i in range(m):
    l=[]
    for j in range(n):
        l.append(0)
    product.append(l)
for i in range(len(mat1)):
    for j in range(len(mat1[i])):
        sum1=0
        for k in range(len(mat1[i])):
            sum1=(sum1)+(mat1[i][k])*(mat2[k][j])
        product[i][j]=sum1
for row in product:
    print(row)