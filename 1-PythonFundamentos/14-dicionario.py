gameFifa = {'name' : 'Fifa 23', 'yearLauch' : 2022, 'gamePrice' : 90.50, 'classification' : 8.5, 'genre' : ['esporte', 'família']}

print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

# 1 - Recuperar um value de um elemento do dicionário
print(gameFifa['classification']) # duas opções para recuperar o elemento
print(gameFifa.get('classification'))

# 2 -Recuperar ou buscar apenas as chaves do dicionário
print(gameFifa.keys())

# 3 - Busca os valores do dicionário
print(gameFifa.values())

# 4 - Buscar itens do dicionário com chave e valor
print(gameFifa.items())

# 5 - Adicionar itens no dicionário
gameFifa['players'] = 2
print(gameFifa)

# 6 - atualizar itens no dicionário
gameFifa.update({"players" : 1})
print(gameFifa)

# 7 - remover item no dicionário
gameFifa.pop('players')
print(gameFifa)