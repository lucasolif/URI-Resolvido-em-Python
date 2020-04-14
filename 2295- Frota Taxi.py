valor_alcool, valor_gasol, rend_alcool, rend_gasol= input().split()

valor_alcool= float(valor_alcool)
valor_gasol= float(valor_gasol)

rend_alcool= float(rend_alcool)
rend_gasol= float(rend_gasol)

x= rend_alcool/valor_alcool
y= rend_gasol/valor_gasol

if x > y:
    print('A')
else:
    print('G')