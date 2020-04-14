n = input()
alt,larg,profun= input().split()

n= int(n)
alt= int(alt)
larg= int(larg)
profun= int(profun)


if (n <= alt) and (n <= larg) and (n <= profun):
    print('S')
else:
    print('N')