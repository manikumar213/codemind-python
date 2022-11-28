s=input()
cd=0
for i in s:
    if i>='0' and i<='9':
        cd+=1
if cd>0:
    print('Contains {} digit'.format(cd))
else:
    print("Doesn't contain digit")