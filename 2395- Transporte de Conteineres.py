A,B,C= input().split()
X,Y,Z= input().split()
A=int(A)
B=int(B)
C=int(C)

X=int(X)
Y=int(Y)
Z=int(Z)

A1=X//A
A2=Y//B
A3=Z//C
total=A1*A2*A3
print(total)
