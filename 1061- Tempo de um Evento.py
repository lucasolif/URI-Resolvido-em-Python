dia1= int(input('Dia '))
h1,m1,s1= map(int,input().split(' : '))

dia2= int(input('Dia '))
h2,m2,s2= map(int,input().split(' : '))

total_segundos =((dia2*86400)+(h2*3600)+(m2*60)+(s2)) - ((dia1*86400)+(h1*3600)+(m1*60)+(s1))
dias= total_segundos//86400
horas= (total_segundos%86400)//3600
minutos= ((total_segundos%86400)%3600)//60
segundos= total_segundos-(dias*86400)-(horas*3600)-(minutos*60)

print(dias,"dia (s)")
print(horas,"hora (s)")
print(minutos,"minuto (s)")
print(segundos,"segundo (s)")
