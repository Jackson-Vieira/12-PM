def solution(n):
    return all(int(d)%2==0 for d in str(n))