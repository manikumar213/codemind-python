n=int(input())
sn=n*n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
x=rev*rev
rev1=0
while x>0:
    r=x%10
    rev1=rev1*10+r
    x=x//10        
if sn==rev1:
    print('True')
else:
    print('False')