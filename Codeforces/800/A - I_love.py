n = int(input())
scores = [int(i) for i in input().split()]
worst = best = 0
ap = 0
for i in range(1, n):
	if scores[i] > scores[best]:
		best =  i 
		ap += 1
	if scores[i] < scores[worst]: 
		worst = i
		ap += 1
 
print(ap)