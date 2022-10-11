n=int(input())
t=n
s=0
while n>0:
    i=1
    fac=1
    r=n%10
    while i<=r:
        fac=fac*i
        i=i+1
    s=s+fac
    n=n//10
if t==s:
    print('The number {} is a strong number'.format(t))
else:
    print('The number {} is not a strong number'.format(t))