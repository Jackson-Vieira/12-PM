def solution(arr):
    aux = 0
    for i in range(1,len(arr)):
        if arr[i] <= arr[i-1]:
            k = arr[i-1]-arr[i]+1
            arr[i] += k
            aux += k
    return aux
            