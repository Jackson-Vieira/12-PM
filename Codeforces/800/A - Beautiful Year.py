y = int(input())
while True:
    y += 1
    if len(str(y)) == len(set(str(y))):
        print(y)
        break