def solve(n):
	if n <= 2:
		return 0
	return n//2-1 if n%2 == 0 else n//2

n = int(input())
for i in range(n):
	n = int(input())
	print(solve(n))