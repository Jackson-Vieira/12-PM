
n = 5
matrix = []
for i in range(5):
	inp = [int(elm) for elm in input().split(" ")]
	matrix.append(inp)


def beatiful_matrix(m):
	size = len(m)
	for i in range(size):
		if 1 in m[i]:
			c = i
			c_r = i+1
			size_l = len(m[i])
			for i in range(size_l):
				if m[c][i] == 1:
					p_c = i+1
	return (abs(3-c_r)+(abs(3-p_c)))

print(beatiful_matrix(matrix))
