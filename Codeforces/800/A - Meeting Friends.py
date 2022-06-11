p = [int(p) for p in input().split()]
p.sort()
print(abs((p[0]+p[2])-(p[0]*2)))