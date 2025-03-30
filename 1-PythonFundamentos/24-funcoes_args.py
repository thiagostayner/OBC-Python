'''
*args -> utilizamos o args quando não temos certeza de quantos argumentos quremos ter na função
    - os argumentos são passados como tupla

**kwargs -> além dos valores podemos passar também as respectivas chaves para cada argumento
    - os argumentos são passados como dicionário
'''

# 1 - soma de números
def soma(*num):
    somaTotal = 0
    for n in num:
        somaTotal += n
    print(f'Soma é: {somaTotal}')

soma(7)
soma(7, 9)
soma (7, 9, 10, 11)

# 2 - Apresentação de cursos
def apresentacao (**data):
    for key, value in data.items():
        print(f'{key} - {value}')

print('###Curso###')

apresentacao(nome='Python', categoria='Backend', level='Iniciante')
apresentacao(nome='Visão Computacional com Python', categoria='IA', level='Avançado')