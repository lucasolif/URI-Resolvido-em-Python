v=float(input())

N100=int(v//100)
v=v%100
N50=int(v//50)
v=v%50
N20=int(v//20)
v=v%20
N10=int(v//10)
v=v%10
N5=int(v//5)
v=v%5
N2=int(v//2)
v=v%2
M1=int(v//1)
v=v%1
M050=int(v//0.50)
v=v%0.50
M025=int(v//0.25)
v=v%0.25
M010=int(v//0.10)
v=v%0.10
M05=int(v//0.05)
v=v%0.05
M01=(v/0.01)
print("NOTAS:")
print(N100,"nota(s) de R$ 100.00")
print(N50,"nota(s) de R$ 50.00")
print(N20,"nota(s) de R$ 20.00")
print(N10,"nota(s) de R$ 10.00")
print(N5,"nota(s) de R$ 5.00")
print(N2,"nota(s) de R$ 2.00")
print("MOEDAS:")
print(M1,"moeda(s) de R$ 1.00")
print(M050,"moeda(s) de R$ 0.50")
print(M025,"moeda(s) de R$ 0.25")
print(M010,"moeda(s) de R$ 0.10")
print(M05,"moeda(s) de R$ 0.05")
print("{:.0f}".format(M01),"moeda(s) de R$ 0.01")