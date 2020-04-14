cred1,cred2,cred3= map(int, input().split())

if (cred1-cred2==0) or (cred2-cred3==0) or (cred1-cred3==0):
    print('S')
elif ((cred1+cred2)-cred3==00) or ((cred2+cred3)-cred1==0) or ((cred3+cred1)-cred2==0):
    print('S')
else:
    print('N')