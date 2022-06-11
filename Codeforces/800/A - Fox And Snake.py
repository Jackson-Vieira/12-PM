n, m = [int(i) for i in input().split()]
aux = 1
b = "."*(m-1)+"#"
print("#"*m)
for c in range(n//2):
	print(b[::aux])
	print("#"*m)
	if aux == 1: aux = -1
	elif aux == -1: aux = 1