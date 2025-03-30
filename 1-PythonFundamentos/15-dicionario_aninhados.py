import pprint

gamesDict = {
    'resident evil 4' : {
        'anoLancamento' : 2023,
        'classificacao' : 9.8,
        'genero' : ['ação', 'aventura']
    },
    'mario odyssey' : {
        'anoLancamento' : 2017,
        'classificacao' : 10.0,
        'genero' : ['aventura', '3d']
    },
    'donkey kong country' : {
        'anoLancamento' : 1995,
        'classificacao' : 9.5,
        'genero' : ['aventura', 'plataforma']
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

# 1 - Buscar informação dentro do dicionário aninhado
print(gamesDict['mario odyssey']['genero'])

# 2 - Adicionar novo item
gamesDict['mario odyssey']['players'] = 1
print(gamesDict['mario odyssey'])

# 3 - excluir um dicionário
del gamesDict['resident evil 4']
pp.pprint(gamesDict)