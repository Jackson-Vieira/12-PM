def solution(s):
    size = len(s)
    for i in range(size-1,-1,-1):
        if s[i] == '(':
            for k in range(i,size):
                if s[k] == ")":
                    s = s[:i]+s[i+1:k][::-1]+s[k+1:]
                    break
    return s