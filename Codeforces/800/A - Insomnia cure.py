def insomnia():
    lst, d = [int(input()) for n in range(4)], int(input())
    d += 1
    null = [0]*d
    divisor = [1]*d
    for i in lst:
        null[::i] = divisor[::i]
    print(sum(null)-1)
insomnia()