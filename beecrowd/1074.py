n = int(input())
numbers = [int(input()) for i in range(n)]
for number in numbers:
    if number == 0:
        print('NULL')
        continue

    if abs(number)%2 == 0:
        print('EVEN', end=' ')
    else:
        print('ODD', end=' ')
    if number < 0:
        print('NEGATIVE')
    else:
        print('POSITIVE')
    