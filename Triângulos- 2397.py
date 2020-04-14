a,b,c= map (int, input().split())

if a>=b+c or b>=a+c or c>=b+a:
    print('n')
elif a**2== b**2+c**2 or b**2== a**2+c**2 or c**2== a**2+b**2:
    print('r')
elif a**2> b**2+c**2 or b**2> a**2+c**2 or c**2> a**2+b**2:
    print('o')
else:
    print('a')
