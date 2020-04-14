p1,p2= map(int, input().split())

if (p2 <= 2 and p2 >= 0):
    print('nova')
elif(p2 <= 100) and (p2 >= 97):
    print('cheia')
elif (p2 > p1):
    print('crescente')
else:
    print('minguante')