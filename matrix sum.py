m1=[[1,2,3],[4,5,6],[7,8,9]]
m2=[[1,1,1],[2,2,2],[3,3,3]]
sum_m=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(m1)):
    for j in range(len(m1[i])):
        sum_m[i][j]=m1[i][j]+m2[i][j]
for row in sum_m:
    print(row)