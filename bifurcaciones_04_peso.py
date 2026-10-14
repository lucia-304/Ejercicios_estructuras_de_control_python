'''
ALGORITMO: CATEGORÍA_DE_ENVÍO_SEGÚN_PESO
ENTRADAS: peso
SALIDA: categoría
SI pedo <= 1:
    categoría = "Sobre"
SI NO:
    SI peso <= 5:
        categoría = "Paquete Pequeño"
    SI NO:
        SI peso <= 20:
            categoría = "Paquete Grande"
        SI NO:
            categoría = "Voluminoso"
'''

def categoria_envio(peso):
    if peso <= 1:
        categoria = "Sobre"
    else:
        if peso <= 5:
            categoria = "Paquete Pequeño"
        else:
            if peso <= 20:
                categoria = "Paquete Grande"
            else:
                categoria = "Voluminoso"
    return categoria

print(categoria_envio(0.5))
print(categoria_envio(3))   
print(categoria_envio(15))
print(categoria_envio(25))