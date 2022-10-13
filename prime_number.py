h=int(input())
f=0
for i in range(1,h+1):
    if h%i==0:
        f+=1
if f==2:
    print('prime')
else:
    print('not a prime')