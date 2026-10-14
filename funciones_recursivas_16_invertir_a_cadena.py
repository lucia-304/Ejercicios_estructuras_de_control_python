'''
ALGORITMO: INVERTIR_UNA_CADENA_DE_TEXTO 
ENTRADAS: cadena
SALIDAS: cadena_invertida
SI len(cadena) = 0:
    cadena_invertida = ""
    SI NO:
        cadena_invertida = cadena[-1] + INVERTIR_UNA_CADENA_DE_TEXTO(cadena[:-1])
DEVOLVER: cadena_invertida
'''
def invertir_cadena(cadena):
    if len(cadena) == 0:
        return ""
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])

print(invertir_cadena("Python"))
