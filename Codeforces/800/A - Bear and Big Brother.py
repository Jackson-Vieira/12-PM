x,y = [int(n) for n in input().split()]
p = 0
while y >= x:
    x,y,p = 3*x,2*y,p+1
print(p)