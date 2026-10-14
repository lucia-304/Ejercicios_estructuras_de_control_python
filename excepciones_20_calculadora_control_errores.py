'''
ALGORITMO: CALCULADORA_CON_CONTROL_DE_ERRORES
ENTRADAS: texto_a, texto_b, operacion
SALIDA: resultado
SI:
    a = REAL(texto_a)
    b = REAL(texto_b
DEVOLVER "Error: valor no numérico"

SI operacion == "suma":
resultado = a + b
SI NO:
SI operacion == "division":
resultado = a / b
resultado = "Error: división entre cero"
DEVOLVER: resultado
'''
def calculadora_control_errores(texto_a, texto_b, operacion): 
    try:
        a = float(texto_a)
        b = float(texto_b)
    except ValueError:
        return "Error: valor no numérico"
    
    if operacion == "suma":
        return a + b
    elif operacion == "division":
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: división entre cero"

print(calculadora_control_errores("10", "0", "division"))
print(calculadora_control_errores("abc", "2", "suma"))
print(calculadora_control_errores("4", "3", "suma"))