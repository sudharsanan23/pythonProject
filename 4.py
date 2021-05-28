s = input()
c = 0
for i in range(0, (len(s) - 1)):
    if s[i] == s[i + 1]:
        c = c + 1
    else:
        if c == 0:
            print(s[i], end="")
        else:
            c = c + 1
            print(s[i] + str(c), end="")
            c = 0
    if i == (len(s) - 2):
        if c == 0:
            print(s[i], end="")
        else:
            c = c + 1
            print(s[i] + str(c), end="")
