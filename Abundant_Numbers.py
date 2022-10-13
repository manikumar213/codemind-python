p=int(input())
z=0
for i in range(1,p):
    if p%i==0:
        z+=i
if z>p:
    print('True')
else:
    print('False')