'''
ALGORITMO: SUCESION_DE_FIBONACCI
ENTRADAS: n
SALIDA: fibonacci
SI n = 0:
    fibonacci = 0
    SI NO:
    SI n = 1:
        fibonacci = 1   
    SI NO:
        fibonacci = SUCESION_DE_FIBONACCI(n - 1) + SUCESION_DE_FIBONACCI(n - 2)
DEVOLVER: fibonacci
'''

def sucesion_de_fibonacci(n):
   if n==0:
      fibonacci = 0
   elif n==1:
      fibonacci = 1
   else:
      fibonacci = sucesion_de_fibonacci(n-1) + sucesion_de_fibonacci(n-2)
   return fibonacci 

print(sucesion_de_fibonacci(6))