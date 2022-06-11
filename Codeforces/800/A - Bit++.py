n =  int(input())
aux = 0
for i in range(n):
	n = input()
	if  n == '++X' or n == 'X++':
		aux += 1
	else:
		aux -= 1
print(aux)