def solution(arr):
    for i in range(2, 1002):
        y = True
        for n in arr:
            if n%i == 0:
                y = False
        if y:
            return i    
