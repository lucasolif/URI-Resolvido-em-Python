dm1,dm2,dm3= map(int, input().split())
altura,largura= map(int, input().split())

if altura >= dm1 and largura >= dm2 or altura >= dm2 and largura >= dm1 or altura >= dm3 and largura >= dm2 or altura >= dm2 and largura >= dm3 or altura >= dm3 and largura >= dm1 or altura >= dm1 and largura >= dm3:
    print('S')
else:
    print('N')