gameName = 'Fifa 23'
gameDescription = '''
Fifa 23 é um jogo de futebol, desenvolvido pela EA Sports,
e que possibilita jogar localmente ou online
'''

print(gameName.upper()) #retorna string em maiúsculo
print(gameName.lower()) #retorna string em minúsculo
print(gameName.capitalize()) #Apenas a primeira letra em maiúsculo
print(gameDescription.capitalize())
print(gameName.title()) #toda primeira letra de uma palavra em maiúsculo
print(gameDescription.title()) #
print(gameName.center(11, '-')) #retorna string centralizada com caractere de preenchimento
print(gameName.find('a')) #retorna a posição de um determinado caractere
print(gameDescription.count('i')) #conta caracteres
print(gameDescription.replace('Fifa', 'Pes')) #altera elemento por outro
print(gameDescription.split(','))