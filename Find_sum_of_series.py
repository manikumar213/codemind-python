a=int(input())
i=1
s=0
while i<=a:
    s=s+(1/i)
    i+=1
print('{:.2f}'.format(s))