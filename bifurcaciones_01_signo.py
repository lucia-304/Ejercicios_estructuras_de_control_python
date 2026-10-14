'''
ALGORITMO: SIGNO_NÚMERO
ENTRADAS: número
SALIDA: signo
SI número = 0:
    signo = "CERO"
    SI NO:
    SI número > 0:
        signo = "POSITIVO"
    SI NO:
        signo = "NEGATIVO"
DEVOLVER: signo
'''
def signo_numero(numero):
    if numero == 0:
        signo = "cero"
    else:
        if numero > 0:
            signo = "positivo"
        else:
            signo = "negativo"
    return signo

print(signo_numero(10)) 
print(signo_numero(-5))
print(signo_numero(0))