def solution(n):
    n = str(n)
    size = len(n)
    return sum([int(num) for num in n[:size//2]]) == sum(int(num) for num in n[size//2:])