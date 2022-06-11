n, h = [int(i) for i in input().split()]
s = sum([int(n) > h for n in input().split()])
print(n-s+s*2)