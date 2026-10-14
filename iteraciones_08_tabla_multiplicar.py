'''
ALGORITMO: TABLA_DE_MULTIPLICAR
ENTRADAS: numero
SALIDA: tabla
tabla = (numero * 1 = numero)
for i in range(2, 11):
     tabla += (numero * i = numero * i)
DEVOLVER: tabla
'''

def tabla_de_multiplicar(numero):
    tabla = f"{numero} * 1 = {numero}"
    for i in range(2, 11):
        tabla += f"\n{numero} * {i} = {numero * i}"
    return tabla

print(tabla_de_multiplicar(3))
