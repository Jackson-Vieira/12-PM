def lexicographically(n,n1):
	if n < n1:
		return '-1'
	if n > n1:
		return '1'
	else:
		return '0'
n = input().upper()
n1 = input().upper()
print(lexicographically(n,n1))