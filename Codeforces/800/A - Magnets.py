n = input();
last = input()
aux = 1
for i in range(int(n)-1):
    inp = input()
    if last != inp :
        aux += 1
    last = inp
print(aux)