from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - Contar itens de uma lista
frutas = ['Maçã', 'Banana', 'Uva', 'Pêra', 'Banana', 'Uva', 'Maçã', 'Laranja', 'Abacaxi', 'Banana', 'Tangerina', 'Uva', 'Pêra', 'Banana']
print(Counter(frutas))

# 2 - utilizando tupla nomeada
game = namedtuple('game', ['name', 'preço', 'nota'])
g1 = game('Fifa23', 90.50, 8.5)
g2 = game('RE4 Remake', 300.00, 10.0)
print(g1)
print(g2)

# 3 - ordenando dicionários
estudantes = {'Pedro':23, 'Ana':22, 'Ronaldo':26, 'Janaína':25}
a = sorted(estudantes.items(), key=itemgetter(0))
print(estudantes)
print(a)

# 4 - utilizando fila com ambas extremidades
deq = deque([20, 40, 60, 80])
deq.appendleft(10)
print(deq)
deq.append(90)
print(deq)
deq.popleft()
deq.pop()
print(deq)