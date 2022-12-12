k = int(input())

total = 0
rabbit = 0
rat = 0
frog = 0

for i in range(k):
    n, l = [n for n in input().split()]
    n = int(n)
    total += n
    if l == 'C':
        rabbit += n
    elif l == 'R':
        rat += n
    elif l == 'S':
        frog += n

data = f'''Total: {total} cobaias
Total de coelhos: {rabbit}
Total de ratos: {rat}
Total de sapos: {frog}
Percentual de coelhos: {(rabbit/total*100):.2f} %
Percentual de ratos: {(rat/total*100):.2f} %
Percentual de sapos: {(frog/total*100):.2f} %'''

print(data)