import random

# 1 - Selecionar valor aleatório de uma lista
lista = [7, 6, 4, 3, 2, 1]
print(random.choice(lista))

# 2 - Gera um número aleatório em um intervalo de valores
r1 = random.randint(1,10)
print(r1)

# 3 - Seleciona caractere aleatório de uma string
name = 'Curso Python'
r3 = random.choice(name)
print(r3)

# 4 - Selecionar mais de um valor aleatório
# sintaxe: random. sample(sequencia, tamanho)
print(random.sample(lista, 2))
s = 'Olá mundo'
print(random.sample(s, 3))