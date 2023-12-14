from random import*  
n=int(input('N='))
m=int(input('M='))
A=[0]*n
cem=0
for i in range(n):
    A[i]=[0]*m
for x in range(n):
    for j in range(m):
        A[x][j]=randint(0,10)
        if x==j :
            cem=cem+A[x][j]
    print(A[x])
print('cem=',cem)
