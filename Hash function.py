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
