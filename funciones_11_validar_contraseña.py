'''
ALGORITMO: VALIDAR_CONTRASEÑA
ENTRADAS: contraseña
SALIDA: es_valida
es_valida = False
if len(contraseña) >= 8:
    es_valida = True
'''

def validar_contraseña(contraseña, longitud_minima=8):
    es_valida = False
    if len(contraseña) >= longitud_minima:
        es_valida = True
    return es_valida

print(validar_contraseña("mi_contraseña_segura"))
print(validar_contraseña("12345, 5"))
print(validar_contraseña("12345"))