k = int(input())


avgs = []
for i in range(k):
    n1, n2, n3 = [float(n) for n in input().split()]
    avg = round(((n1*2)+(n2*3)+(n3*5)) / 10, 1)
    avgs.append(avg)

for avg in avgs:
    print(avg)