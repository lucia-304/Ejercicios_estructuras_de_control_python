'''
ALGORITMO: TEXTO_EN_MAYÚSCULAS_Y_NÚMERO_DE_PALABRAS
ENTRADAS: frase
SALIDA: frase_mayusculas, numero_de_palabras
frase_mayusculas = frase.upper()
numero_de_palabras = len(frase.split())
DEVOLVER: frase_mayusculas, numero_de_palabras
'''

def texto_en_mayusculas_y_numero_de_palabras(frase):
    frase_mayusculas = frase.upper()
    numero_de_palabras = len(frase.split())
    return frase_mayusculas, numero_de_palabras

print(texto_en_mayusculas_y_numero_de_palabras("Hola mundo, estoy usando Python"))
