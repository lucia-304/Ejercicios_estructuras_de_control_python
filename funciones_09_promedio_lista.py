'''
ALGORITMO: PROMEDIO_DE_UNA_LISTA_DE_NÚMEROS
ENTRADAS: lista
SALIDA: promedio
suma = 0
for número in lista:
    suma += número
promedio = suma / len(lista)
DEVOLVER: promedio
'''

def promedio_de_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero 
        promedio = suma / len(lista)
    return promedio

print(promedio_de_lista([4, 8, 6]))