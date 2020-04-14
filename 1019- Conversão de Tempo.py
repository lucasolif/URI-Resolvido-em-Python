segundo= int(input())
Horas= segundo//3600
Minutos= (segundo%3600)//60
Segundos= segundo-(Horas*3600)-(Minutos*60)
print("{}:{}:{}".format(Horas,Minutos,Segundos))

