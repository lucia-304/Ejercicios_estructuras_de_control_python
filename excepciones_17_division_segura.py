'''
ALGORITMO: DIVISIÓN_SEGURA
ENTRADAS: dividendo, divisor
SALIDA: resultado
SI divisor = 0:
    resultado = "Error: División entre cero."
    SI NO:
        resultado = dividendo / divisor
DEVOLVER: resultado
'''

def division_segura(dividendo, divisor):
    try:
        return dividendo / divisor
    except ZeroDivisionError:
        return "Error: División entre cero."

print(division_segura(10, 2))
print(division_segura(10, 0))