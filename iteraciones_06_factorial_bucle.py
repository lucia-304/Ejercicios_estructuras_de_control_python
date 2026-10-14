'''
ALGORITMO: FACTORIAL_DE_NÚMERO
ENTRADAS: n 
SALIDA: factorial
factorial = 1
for i in range(1, n + 1):   
    factorial *= i          
DEVOLVER: factorial
'''

def factorial_de_numero(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

print(factorial_de_numero(5))
print(factorial_de_numero(20))
print(factorial_de_numero(0))