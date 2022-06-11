def solution(m):
    n_lines = len(m)
    n_cols = len(m[0])
    total = 0
    for j in range(n_cols):
        for i in range(n_lines):
            if m[i][j] != 0:
                total += m[i][j]
            else:
                break
    return total
