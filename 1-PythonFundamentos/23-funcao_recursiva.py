'''
Fatorial de um número
1 -> 1
3 -> 3 * 2 * 1
5 -> 5 * 4 * 3 * 2 * 1
'''

# 1 - Fatorial de um número
def factorial (num):
    if num == 1:
        return 1
    else:
        return (num * factorial (num - 1))

numero = int(input('Digite o número para o fatorial: '))
print(f'O fatorial de {numero} é: {factorial(numero)}')

# 2 - Soma total de um número
'''
3 -> 3 + 2 + 1
5 -> 5 + 4 + 3 + 2 + 1
'''

def soma (num):
    if num == 1:
        return 1
    else:
        return (num + soma(num - 1))
    
numero1 = int(input('Digite um número para ver sua soma: '))
print(f'A soma total do {numero1} é: {soma(numero1)}')