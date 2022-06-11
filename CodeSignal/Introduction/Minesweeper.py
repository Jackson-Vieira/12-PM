def solution(matrix):
    lines, cols = len(matrix), len(matrix[0])
    construct = [[0 for i in range(cols)] for i in range(lines)] # Create a new Matrix

    def defineArea(l, c):
        for j in range(l-1,l+2):
            for k in range(c-1, c+2):
                if (0 <= j < lines) and (0 <= k < cols) and (j,k) != (l,c):
                    construct[j][k] += 1
        
    for j in range(lines):
        for k in range(cols):
            if matrix[j][k]:
                defineArea(j,k)
                
    return construct