n = int(input())
l = []
for i in range(n):
    if i%2 == 0:
        l.append('I hate')
    else:
        l.append('I love')
print((" that ".join(l))+" it")