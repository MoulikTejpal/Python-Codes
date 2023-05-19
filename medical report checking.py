safelimits={}
n=int(input('Enter the no. of tests'))
for i in range(n):
    testname=input('Enter test name')
    minimum=float(input())
    maximum=float(input())
    safelimits[testname]=(minimum,maximum)
for row in safelimits:
    print(row,safelimits[row])
testtaken=input()
observed=float(input())
ran=safelimits[testtaken]
print(ran)
if ran[0]<observed<ran[1]:
    print('Normal')
else:
    print('Abnormal')