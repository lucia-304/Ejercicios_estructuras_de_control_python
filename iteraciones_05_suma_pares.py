'''
ALGORITMO: SUMA_DE_PARES_ENTRE_1_Y_N
ENTRADAS: n
SALIDA: suma
suma = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        suma += i   

DEVOLVER: suma
'''

def suma_de_pares(n):
    suma = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            suma += i
    return suma

print(suma_de_pares(1))
print(suma_de_pares(10))
print(suma_de_pares(75))