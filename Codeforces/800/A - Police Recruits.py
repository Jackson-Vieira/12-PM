n, dp = int(input()), map(int, input().split())
ap = c = unrc = 0
for elm in dp:
    if elm == -1:
        c += 1
    else:
        ap += elm

    if c > 0 and ap < 1:
        unrc += 1
        c -= 1
    
    if c>0 and ap>0:
        c -= 1
        ap -= 1

print(unrc)