aux = 0
while aux <= 2:
    for k in range(1, 4):
        i = round(aux, 1)
        j = round(k+aux, 1)
        if i%1 <= 0: i = int(i)
        if j%1 <= 0: j = int(j)
        print(f'I={i} J={j}',)
    aux += 0.2