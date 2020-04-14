cod_peca1,quant_peca1,valor_peca1=input().split()
cod_peca2,quant_peca2,valor_peca2=input().split()

quant_peca1=int(quant_peca1)
quant_peca2=int(quant_peca2)

valor_peca1=float(valor_peca1)
valor_peca2=float(valor_peca2)

total=(quant_peca1 * valor_peca1) + (quant_peca2 * valor_peca2)
print("VALOR A PAGAR: R$","{:.2f}".format(total))
