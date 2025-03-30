gameName = input('Digite o nome do jogo: ')
nota = 0
qtdeNotas = 0
totalNotas = 0
media = 0

while nota != -1:
    nota = float(input('Digite a nota do jogo: '))
    if nota != -1:
        totalNotas += nota
        qtdeNotas += 1
        media = totalNotas / qtdeNotas
print(f'Médias das avaliações do jogo {gameName} é {media:.2f}')
