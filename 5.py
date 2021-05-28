a = input()
b = input()
for i in a:
    if i not in b:
        print(i)
for j in b:
    if j not in a:
        print(j)

