n=int(input())
is_negative=0
if n<0:
    is_negative=1
    n=-n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if is_negative==1:
        print(-rev)
else:
        print(rev)