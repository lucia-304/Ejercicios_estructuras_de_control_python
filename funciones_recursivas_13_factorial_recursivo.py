'''
ALGORITMO: FACTORIAL_RECURSIVO
ENTRADAS: n
SALIDA: factorial
 SI n = 0 O n = 1:
    factorial = 1
    SI NO:
        factorial = n * FACTORIAL_RECURSIVO(n - 1)
DEVOLVER: factorial
'''

def factorial_recursivo(n):
    if n == 0 or n == 1:
        return  1
    else:
        return n * factorial_recursivo(n - 1)

print(factorial_recursivo(5))
print(factorial_recursivo(20))