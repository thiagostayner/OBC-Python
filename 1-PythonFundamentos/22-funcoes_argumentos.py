# 1 - Crie uma função que receba dois argumentos: o primeiro nome e o segundo nome

def fullName(fname, lname):
    print(f'Nome completo: {fname} {lname}')

fullName('Rodrigo', 'Macedo')

# 2 - Crie uma função que some dois números via parâmetros
def soma (a,b):
    return a + b

print(soma(10,50))

# 3 - Argumentos padrões numa função
def endereco(pais='Brasil'):
    print(f'Eu moro no {pais}')

endereco()
endereco('Espanha')
# 4 - Avaliação do jogo

def notaJogo(qtdNotas):
    nomeJogo = str(input('Digite o nome do jogo: '))
    soma = 0
    for i in range (qtdNotas):
        notas = float(input(f'Digite a {i + 1}ª nota: '))
        soma += notas
    print(f'Média de avaliação do jogo {nomeJogo} é: {soma / qtdNotas}')

avaliacoes = int(input('Digite quantas avaliações deseja fazer do jogo: '))
notaJogo(avaliacoes)
