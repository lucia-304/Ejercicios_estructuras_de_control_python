'''
ALGORITMO: CONVERSIÓN_DE_TEMPERATURA
ENTRADAS: temperatura, unidad_origen, unidad_destino
SALIDA: temperatura_convertida
convertir_celsius_a_fahrenheit = (temperatura * 9/5) + 32
convertir_fahrenheit_a_celsius = (temperatura - 32) * 5/9   
DEVOLVER: temperatura_convertida
'''

def convertir_celsius_a_fahrenheit(temperatura):
    return (temperatura * 9/5) + 32
def convertir_fahrenheit_a_celsius(temperatura):
    return (temperatura - 32) * 5/9

print (convertir_celsius_a_fahrenheit(0))  
print (convertir_fahrenheit_a_celsius(32))

