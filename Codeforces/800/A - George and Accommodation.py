c = 0
for i in range(int(input())):
    p,q =[int(n) for n in input().split()]
    c += (q-p >= 2)
print(c)