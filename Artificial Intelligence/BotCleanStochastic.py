x, y = list(map(int, input().split()))
a = [0] * 5
for i in range(5):
    a[i] = input()
    a[i].find('d')
    if a[i].find('d') == -1:
        continue
    x1, y1 = i, a[i].find('d')
if x < x1:
    print('DOWN')
elif x > x1:
    print('UP')
elif y < y1:
    print('RIGHT')
elif y > y1:
    print('LEFT')
else:
    print('CLEAN')