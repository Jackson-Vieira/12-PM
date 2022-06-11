def solution(image):
    l = len(image)
    c = len(image[0])

    m = []

    for k in range(l-2):
        aux = []
        for i in range(c-2):
            average = sum(image[k][i:i+3])+sum(image[k+1][i:i+3])+sum(image[k+2][i:i+3])
            aux.append(average//9)
        
        m.append(aux)
    return m