def solution(arr):
    n = 0
    size = len(arr)
    for i in range(size-1):
        if arr[i] >= arr[i+1]:
            n += 1
            if 0 < i < size-2:
                if arr[i+1] <= arr[i-1] and arr[i] >= arr[i+2]:
                    return False
    return n <= 1