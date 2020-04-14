k= int(input())

if k==1:
    print('Top 1')
elif 1 < k <= 3:
    print('Top 3')
elif 3 < k <= 5:
    print('Top 5')
elif 5 < k <= 10:
    print('Top 10')
elif 10 < k <= 25:
    print('Top 25')
elif 25 < k <= 50:
    print('Top 50')
else:
    print('Top 100')