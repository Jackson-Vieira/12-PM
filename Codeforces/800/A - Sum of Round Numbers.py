numbers = [int(input()) for n in range(int(input()))]
 
 
for k in numbers:
	aux, r = 10, []
	n = k
	
	while n // aux != 0:
		if n%aux != 0:
			r.append(str(n%aux))
			n -= n%aux
		aux *= 10
	r.append(str(n))
	print(len(r))
	print(" ".join(r))