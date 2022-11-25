n=int(input())
z=list(map(int,input().split()))
a=int(input())
c = 0
for i in range(len(z)):
    if a==z[i]:
        c += 1
print(c)
