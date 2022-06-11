k, r = [int(n) for n in input().split()]
 
c = 1
while ((k*c)%10)-r != 0 and (k*c)%10 != 0:
    c += 1
print(c)
