def solution(name):
    if (name[0].isnumeric()) == False:
        aux = [0,0]
        for l in name:
            if l == "_":
                continue
            if l.isalnum():
                continue
            return False
        return True
    return False