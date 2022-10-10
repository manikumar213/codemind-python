n=int(input())
pod=1
sod=0
while n>0:
    r=n%10
    pod*=r
    sod+=r
    n=n//10
    x=pod-sod
print(x)