'''
ALGORITMO: SUMA_RECURSIVA_DE_UNA_LISTA
ENTRADAS: lista
SALIDA: suma
SI lista está vacía:
    suma = 0
    SI NO:
        suma = lista[0] + SUMA_RECURSIVA_DE_UNA_LISTA(lista[1:])
DEVOLVER: suma

'''

def suma_lista(números):
    if not números:
        suma = 0 
    else: 
        suma = números[0] + suma_lista(números[1:])
    return suma

print (suma_lista([1, 2, 3, 4]))
