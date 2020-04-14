consumo= input()

consumo= int(consumo)
taxa= 7

if consumo <= 10:
    print(taxa)
elif 10 < consumo <= 30:
    x = (consumo-10)*1 + taxa
    print(x)
elif 30 < consumo <= 100:
    x= (consumo-30)*2 + 27
    print(x)
elif consumo > 100:
    x= (consumo-100)*5 + 167
    print(x)