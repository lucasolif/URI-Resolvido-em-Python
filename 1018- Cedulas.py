v= int(input())
N100=v//100
N50=v%100//50
N20=v%100%50//20
N10=v%100%50%20//10
N5=v%100%50%20%10//5
N2=v%100%50%20%10%5//2
N1=v%100%50%20%10%5%2
print(v)
print(N100,"nota(s) de R$ 100,00")
print(N50,"nota(s) de R$ 50,00")
print(N20,"nota(s) de R$ 20,00")
print(N10,"nota(s) de R$ 10,00")
print(N5,"nota(s) de R$ 5,00")
print(N2,"nota(s) de R$ 2,00")
print(N1,"nota(s) de R$ 1,00")