def solution(a, b):
    return sorted(a) == sorted(b) and sum([a[i]!=b[i] for i in range(len(a))])<=2