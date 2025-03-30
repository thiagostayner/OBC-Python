gamesTuple = ('Fifa 23' , 'Red Dead 2', 'Star Wars', 'Mario Odyssey', 'The Legend of Zelda')

print(gamesTuple)
print(type(gamesTuple))

# Não possibilita adicionar valores na tupla
# Nâo pode remover valores
# Não pode ordenar
# A tupla é imutável 

# 1 - Buscar os dois primeiros itens da tupla
print(gamesTuple[:2])

# 2 - Buscar o último item da tupla
print(gamesTuple[-1])

# 3 - Buscar jogos até uma determinada posição
print(gamesTuple[0:3])

# 4 - Buscar jogos de uma posição em diante
print(gamesTuple[2:])

# 5 - Recuperar um item pelo indice
print(gamesTuple.index('Red Dead 2'))