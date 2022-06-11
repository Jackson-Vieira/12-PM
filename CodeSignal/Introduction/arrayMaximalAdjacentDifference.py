def solution(iA):
    best = abs(iA[0]-iA[1])
    for i in range(1,len(iA)-1):
        best = max(best, abs(iA[i]-iA[i+1]))
    return best