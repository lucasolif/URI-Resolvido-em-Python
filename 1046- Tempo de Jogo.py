t1, t2= map(int, input().split())

if t1 > t2:
    x= 24-t1
    y= x + t2
    print('O JOGO DUROU',"{}".format(y),'HORA(S)')
elif t2 > t1:
    x= t2-t1
    print('O JOGO DUROU','{}'.format(x),'HORA(S)')
elif t1==t2:
    x= 24
    print('O JOGO DUROU','{}'.format(x),'HORA(S)')