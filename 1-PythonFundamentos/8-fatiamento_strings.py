gameName = 'Fifa 23'
gameDescription = '''
Fifa 23 é um jogo de futebol desenvolvido pela EA Sports
e que possibilita jogar localmente ou online
'''

# string[inicio:fim] - índice começa na posição 0 | ídice final -1

# 1 - Bucando toda string a partir da primeira posição
print(gameName[0:])

# 2 - Busque toda string até a última posição
print(gameName[:7])

# 3 - Busqe toda string da terceira até a última posição
print(gameName[2:])

'''
string[inicio:fim:passo] - índice começa na posição 0 | ídice final -1
passo - determina o incremento. Por padrão o passo é 1
'''

# 4 - Busque toda string de 2 em 2 caracteres
print(gameName[::2])

# 5 - Busque toda a string nos índices ímpares
print(gameName[1::2])

# 6 - Inverter uma string
print(gameName[::-1])