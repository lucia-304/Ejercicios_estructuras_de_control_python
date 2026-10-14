'''
ALGORITMO: MAYOR_DE_TRES_NUMEROS
ENTRADAS: a, b, c
SALIDA: mayor
SI a > b:   
    SI a > c:
        mayor = a
    SI NO:
        mayor = c   
SI NO:
    SI b > c:
        mayor = b
    SI NO:
        mayor = c
DEVOLVER: mayor
'''

def mayor_de_tres(a, b, c):
    if a > b:
        if a > c:
            mayor = a
        else:
            mayor = c
    else:
        if b > c:
            mayor = b
        else:
            mayor = c
    return mayor

print(mayor_de_tres(7, 7, 3))
print(mayor_de_tres(4, 9, 2))
print(mayor_de_tres(1, 2, 3))