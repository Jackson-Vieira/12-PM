n = int(input())
for t in range(n):
    a, b = [int(n) for n in input().split()]
    
    m = 0
    i = 10
 
    dif = abs(a-b)
    while i > 0:
       
        m += dif//i
 
 
        if dif%i == 0:
            break   
        
        dif -= (dif//i)*i
 
        i -= 1
    print(m)