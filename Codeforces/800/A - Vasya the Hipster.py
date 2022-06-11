a, b =  map(int, input().split())
f = max(a,b) - min(a,b)
print(min(a,b), end = " ")
print(0 if f <= 1 else f//2)