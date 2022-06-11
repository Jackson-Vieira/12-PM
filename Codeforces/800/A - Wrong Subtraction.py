n,k = [int(elm) for elm in input().split()]

for o in range(k):
	if  n%10 != 0:
		n -= 1
	else:
		n = n//10
print(n)