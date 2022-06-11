for i in range(int(input())):
    n = input()
    if len(n) > 2:
        n += n[-1]
        print(n[::2])
    else:
        print(n)