n = int(input());c = input();p=0
for i in range(n-1):
    if c[i] == c[i+1]:
        p += 1
print(p)