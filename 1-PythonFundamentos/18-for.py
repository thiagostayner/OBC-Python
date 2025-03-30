gameList = ['Fifa', 'God of War', 'Red Dead 2', 'Unhcarted']

# 1 iterando valores de uma lista
for game in gameList:
    print(game)

# 2 Quando a condição for atendida, o loop será encerrado
for game in gameList:
    if game == 'Red Dead 2':
        break
    print(game)

# 3 Quando a condição for atendida, o Loop vai para a próxima iteração
for game in gameList:
    if game == 'Red Dead 2':
        continue
    print(game)

# 4 Avaliação do jogo
gameName = str(input('Digite o nome do jogo: '))
gameRating = int(input('Digite quantas avaliações deseja fazer no jogo: '))

sum = 0

for i in range(gameRating):
    nota = float(input('Digite a nota que você da para o jogo: '))
    sum += nota

media = sum / gameRating
print(f'A média da nota para o jogo {gameName} é {media:.2f}')
