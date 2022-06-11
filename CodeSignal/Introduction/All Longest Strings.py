def solution(arr):
    new_list = []
    best = 0
    for elm in arr:
        aux = len(elm)
        if aux > best:
            best = aux
            new_list = []
            new_list.append(elm)

        elif aux == best:
            new_list.append(elm)
        
    return new_list