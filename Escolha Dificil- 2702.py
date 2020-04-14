frango, bife, massa = input().split()
ref1, ref2, ref3 = input().split()

frango = int(frango)
bife = int(bife)
massa = int(massa)

ref1 = int(ref1)
ref2 = int(ref2)
ref3 = int(ref3)

if ref1 > frango and ref2 > bife and ref3 > massa:
    print((ref1 - frango) + (ref2 - bife) + (ref3 - massa))
elif ref1 < frango and ref2 > bife and ref3 > massa:
    print((ref2 - bife) + (ref3 - massa))
elif ref1 > frango and ref2 < bife and ref3 > massa:
    print((ref1-frango) + (ref3 - massa))
elif ref1 > frango and ref2 > bife and ref3 < massa:
    print((ref1 - frango) + (ref2 - bife))
elif ref1 > frango and ref2 < bife and ref3 < massa:
    print((ref1 - frango))
elif ref1 < frango and ref2 < bife and ref3 > massa:
    print((ref3 - massa))
elif ref1 < frango and ref2 > bife and ref3 < massa:
    print((ref2 - bife))
else:
    ref1 == frango and ref2 == bife and ref3 == massa
    print('0')
