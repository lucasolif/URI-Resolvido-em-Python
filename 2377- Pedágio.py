compri_estrada,distanc_pedagio= input().split()
custo_quilo,valor_pedag= input().split()

compri_estrada= int(compri_estrada)
distanc_pedagio= int(distanc_pedagio)

custo_quilo= int(custo_quilo)
valor_pedag= int(valor_pedag)

custo_pedag= (compri_estrada//distanc_pedagio)*valor_pedag
valor_gasol= compri_estrada*custo_quilo
total= (custo_pedag+valor_gasol)
print(total)