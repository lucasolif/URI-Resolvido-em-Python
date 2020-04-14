minutos_restante= int(input())
minuto1,minuto2= input().split()

minuto1= int(minuto1)
minuto2= int(minuto2)

soma_minutos= minuto1+minuto2

if minutos_restante>=soma_minutos:
    print("Farei hoje!")
else:
    print("Deixa para amanha!")
