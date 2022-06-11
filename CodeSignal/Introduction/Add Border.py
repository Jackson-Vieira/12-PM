def solution(picture):
    size = len(picture[0])+2
    return ["*"*size]+["*"+elm+"*" for elm in picture]+["*"*size]