team={}
n_t=int(input('enter no. of teams'))
n_p=int(input('enter no. of players'))
for i in range(n_t):
    t=input('enter team name')
    l=[]
    for j in range(n_p):
        p=input('enter player name')
        l.append(p)
    team[t]=l
check=input('enter name of the team whose player list is required')
print('The players list:',team[check])