def solution(arr):
    best = arr[0]*arr[1]
    
    for i in range(1,len(arr)-1):
        best = max(best, arr[i]*arr[i+1])
    return best