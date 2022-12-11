numbers = []
for i in range(6):
    n = float(input())
    if n > 0: 
        numbers.append(n)
print(f'{len(numbers)} valores positivos')    
print('{:.1f}'.format(sum(numbers)/len(numbers)))