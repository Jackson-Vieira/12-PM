n = int(input())
r = []
for i in range(n):
    a,b = input().split()
    a,b = int(a),int(b)
    if a%b != 0:
        r.append(b-(a%b))
    else:
        r.append(0)
for i in r: print(i)
