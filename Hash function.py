a=[3,2,9,6,11,13,7,12]
m=10
b=[]

for i in range(len(a)):
    k=a[i]
    n=((2*k)+3)%10
    b.append(n)
    for j in range(m):
        if b[j]==j:
            b[j]=



