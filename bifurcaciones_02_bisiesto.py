'''
ALGORITMO: AÑO_BISIESTO
ENTRADAS: año
SALIDA: mensaje
SI año es divisible por 4:
    SI año es divisible por 100:
        SI año es divisible por 400:
            mensaje = "El año es bisiesto"
        SI NO:
            mensaje = "El año no es bisiesto"
    SI NO:
        mensaje = "El año es bisiesto"
SI NO:
    mensaje = "El año no es bisiesto"
DEVOLVER: mensaje
'''

def es_bisiesto(año): 
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                mensaje = "El año es bisiesto"
            else:
                mensaje = "El año no es bisiesto"
        else:
            mensaje = "El año es bisiesto"
    else:
        mensaje = "El año no es bisiesto"
    return mensaje

print(es_bisiesto(2020))
print(es_bisiesto(1900))