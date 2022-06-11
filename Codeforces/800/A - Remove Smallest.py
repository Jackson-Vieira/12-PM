def solve(arr, n):
    status = True
    for i in range(n-1):
        if abs(arr[i]-arr[i+1]) > 1:
            print("NO")
            status = False
            break
    if status:
        print("YES")
 
n = int(input())
for k in range(n):
    n = int(input())
    arr = [int(elm) for elm in input().split()]
 
    arr.sort()
    solve(arr, n)