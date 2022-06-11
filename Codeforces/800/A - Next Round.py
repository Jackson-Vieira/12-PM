n,k = [int(i) for i in input().split()]
s = [int(i) for i in input().split()]
k_place = s[k-1]
p = 0
for i in range(n):
	if s[i] < k_place:
		break
	if s[i] >= k_place and s[i] > 0:
		p += 1
print(p)