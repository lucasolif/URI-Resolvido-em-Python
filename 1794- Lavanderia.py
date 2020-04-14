num= int(input())

x1,x2= map(int, input().split())
y1,y2= map(int, input().split())

if  x1 <= num <= x2 and y1 <= num <= y2:
    print('possivel')
else:
    print('impossivel')
