def solution(arr):
    size = len(arr)
    for i in range(size):
        if arr[i] != -1:
            for k in range(i+1,size):
                if arr[i] > arr[k] and arr[k] != -1:
                    arr[i],arr[k] = arr[k],arr[i]               
    return arr