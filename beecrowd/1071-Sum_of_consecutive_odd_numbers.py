values = int(input()), int(input())

s= 0
for i in range(min(values)+1, max(values)):
    if i%2:
        s+=i

print(s)