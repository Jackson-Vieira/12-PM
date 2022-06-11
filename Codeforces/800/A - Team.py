n =  int(input())
p = 0
for i in range(n):
	n1 = [int(i) for i in input().split()]
	y = sum(n1)
	if y >= 2:
		p += 1
print(p)