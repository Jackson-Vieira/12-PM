maxi = cr = 0
for k in range(int(input())-1):
	a,b = [int(elm) for elm in input().split()]
	cr += b-a
	if cr > maxi:
		maxi = cr
print(maxi)
		