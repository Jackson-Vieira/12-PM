n = int(input())
soldiers = [int(elm) for elm in input().split()]
mx,mn = max(soldiers), min(soldiers)
mx = soldiers.index(mx)
mn = (n-1)-soldiers[::-1].index(mn)
print((mx+((n-1)-mn))-1 if mn < mx else mx+((n-1)-mn))