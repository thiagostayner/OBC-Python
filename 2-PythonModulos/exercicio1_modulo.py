'''
Módulo de Strings

-> Escreva um módulo em python para tratar algumas strings e que possua as seguintes funcionalidades:
1. Inverter uma string de trás para frente.
2. Retornar apenas letras com índice par.
3. Retornar apenas letras com índice ímpar
'''

def inverte (a):
    palavra = a[::-1]
    return(palavra)

def indice_par (a):
    palavra = a[::2]
    return palavra

def indice_impar (a):
    palavra = a[1::2]
    return palavra
