inputs = list(map(int, input().split()))
n = max(inputs)
for i in inputs:
    if i != n:
        print(n-i, end=" ")