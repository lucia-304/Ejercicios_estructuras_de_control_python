'''
ALGORUTMO: ACCESO_SEGUR0_A_UNA_LISTA
ENTRADAS: lista, índice
SALIDA: elemento
SI índice está dentro del rango de la lista:
    elemento = lista[índice]
    SI NO:
        elemento = "Error: Posición fuera de rango."  
DEVOLVER: elemento
'''

def acceso_seguro(lista, índice):
    try:
        return lista[índice]
    except IndexError:
        return "Error: Posición fuera de rango."

print(acceso_seguro([1, 2, 3], 1))
print(acceso_seguro([1, 2, 3], 5))