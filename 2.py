k = list(map(int, input().split()))
a = int(input())
n = len(k)
b = None
for i in range(0, n):
    for j in range(i + 1, n):
        if k[i] + k[j] == a:
            print(k[i], k[j])
            b = 1
            break
    if b == 1:
        break
if b != 1:
    print('No Pairs found')
