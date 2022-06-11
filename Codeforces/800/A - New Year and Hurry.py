n, k = [int(i) for i in input().split()]
aux = 0
for p in range(1, n+1):
	aux += p*5
	if aux > (240-k):
		n -= 1
print(n)