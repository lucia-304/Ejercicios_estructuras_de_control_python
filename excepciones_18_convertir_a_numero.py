'''
ALGORITMO: CONVERTIR_TEXTO_A_NÚMERO
ENTRADAS: cadena
SALIDA: número
SI cadena es un número válido:
    número = float(cadena)
    SI NO:
        número = "Error: No es un número."
DEVOLVER: número
'''

def convertir_a_numero(cadena):
    try:
        return float(cadena)
    except ValueError:
        return "Error: No es un número."

print(convertir_a_numero("42"))
print(convertir_a_numero("hola"))