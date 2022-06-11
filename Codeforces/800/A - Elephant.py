s = int(input());
x=5;y=0;
while s > 0:
	y += s//x
	s = s%x
	x -= 1
 
print(y)