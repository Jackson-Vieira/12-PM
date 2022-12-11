n = int(input())
out = 0
for i in range(n):
    number = int(input())
    if not (number >= 10 and number <= 20):
        out += 1
    
print(f'{n-out} in')
print(f'{out} out')