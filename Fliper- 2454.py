porta_1,porta_2= input().split()

porta_1= int(porta_1)
porta_2= int(porta_2)

if porta_1==1 and porta_2==0:
    print('B')
elif porta_1==1 and porta_2==1:
    print('A')
else:
    print('C')