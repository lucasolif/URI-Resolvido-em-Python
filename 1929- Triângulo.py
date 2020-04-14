a,b,c,d= map(int, input().split())

if abs(b-c)<a<b+c or abs(b-d)<a<b+d or abs(c-d)<a<c+d:
    print('S')
elif abs(a-c)<b<a+c or abs(a-d)<b<a+d or abs(d-c)<b<d+c:
    print('S')
elif abs(b-a)<c<b+a or abs(b-d)<c<b+d or abs(a-d)<c<a+d:
    print('S')
elif abs(a-b)<d<a+b or abs(c-b)<d<c+b or abs(c-a)<d<c+a:
    print('S')
else:
    print('N')