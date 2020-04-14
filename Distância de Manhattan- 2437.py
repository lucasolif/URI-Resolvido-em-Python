cord_1,cord_2,reun_1,reun_2= input().split()

cord_1= int(cord_1)
cord_2= int(cord_2)
reun_1= int(reun_1)
reun_2= int(reun_2)

n_cruzamento=abs(reun_1-cord_1) + abs(reun_2-cord_2)
print(n_cruzamento)