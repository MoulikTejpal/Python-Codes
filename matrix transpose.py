m=[[1,2,3],[4,5,6],[7,8,9]]
t=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(m)):
    for j in range(len(m[i])):
        t[j][i]=m[i][j]
for row in t:
    print(row)