coins = [1, 5, 10, 20, 100]
n = int(input())
def solve(n):
    k = 0
    for c in coins[::-1]:
        
        k += n//c
        n = n%c

    return k

print(solve(n))