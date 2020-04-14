D= int(input())
Anos= D//365
Meses= (D%365)//30
Dias= D-(Anos*365)-(Meses*30)
print(Anos,"ano(s)")
print(Meses,"mes(es)")
print(Dias,"dia(s)")