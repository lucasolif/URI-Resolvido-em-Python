cod, quant= map(int, input().split())

cod1= 4.00
cod2= 4.50
cod3= 5.00
cod4= 2.00
cod5= 1.50

if cod==1:
    total= quant*cod1
    print("Total: R$","{:.2f}".format(total))
elif cod==2:
    total= quant*cod2
    print("Total: R$","{:.2f}".format(total))
elif cod==3:
    total= quant*cod3
    print("Total: R$","{:.2f}".format(total))
elif cod==4:
    total= quant*cod4
    print("Total: R$","{:.2f}".format(total))
else:
    cod==5
    total= quant*cod5
    print("Total: R$","{:.2f}".format(total))
