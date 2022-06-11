n  = int(input());
print("I become the guy." if sorted(list(set([int(elm) for elm in input().split()[1:]+input().split()[1:]]))) == [num for num in range(1,n+1)] else "Oh, my keyboard!")