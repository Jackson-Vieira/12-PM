var = input()+input()
aux = input()
print("YES" if all([var.count(l) == aux.count(l) for l in var]) and len(var) == len(aux) else "NO")
