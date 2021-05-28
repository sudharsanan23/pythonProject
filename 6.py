import random

a = []
A = int(input())
for i in range(A):
    n = random.sample(range(0, A), A)
    a.append(n)
    s = []
for i in range(A):
    x = input('enter name')
    a.append(x)
for i in range(A):
    print("Day-", i + 1, end=' ')
    for j in range(A):
        c = a[i][j]
        print(a[c], end=' ')
        print("\n")
