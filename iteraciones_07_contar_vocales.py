'''
ALGORITMO: CONTAR_VOCALES_DE_UNA_PALABRA
ENTRADAS: palabra
SALIDA: cantidad_vocales
cantidad_vocales = 0
for letra in palabra:
    SI letra es una vocal:
        cantidad_vocales += 1
DEVOLVER: cantidad_vocales
'''

def contar_vocales(palabra):
    cantidad_vocales = 0
    for letra in palabra:
        if letra.lower() in 'aeiou':
            cantidad_vocales += 1
    return cantidad_vocales

print(contar_vocales("Hola"))
print(contar_vocales("Python"))
print(contar_vocales("ROJO"))
print(contar_vocales("iteraciones"))
print(contar_vocales("xyz"))