"""a=[3,2,9,6,11,13,7,12]
m=10
b=[]
v=[]
for i in range(len(a)):
    k=a[i]
    n=((2*k)+3)%10
    b.append(n)
    for j in range(0,9):
        if b[j]==j:
            v[j]=a[i]
print(v)
"""

li=list(map(int,input().split()))
m=int(input())
v=[]
for i in range(m):
    v.append([i,[]])
for i in li:
    n=((2*i)+3)%10
    if n<m:
        v[n][1].append(i)
for i in v:
    print(i)
