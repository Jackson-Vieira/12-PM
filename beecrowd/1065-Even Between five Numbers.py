pares = impares = negativos = positivos = 0
for i in range(5):
    n = int(input())
    if n%2 == 0:
        pares += 1 
    else:
        impares += 1
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1

print(f'''{pares} valor(es) par(es)
{impares} valor(es) impar(es)
{positivos} valor(es) positivo(s)
{negativos} valor(es) negativo(s)''')