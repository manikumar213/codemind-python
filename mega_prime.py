x=int(input())
is_prime=True
for i in range(2,int(x**0.5)+1):
    if x%i==0:
        is_prime=False
        break
isdigits_prime=True
while x>0:
    r=x%10
    if r!=2 and r!=3 and r!=5 and r!=7:
        isdigits_prime=False
        break
    x=x//10
if is_prime and isdigits_prime:
    print('Mega Prime')
else:
    print('Not Mega Prime')