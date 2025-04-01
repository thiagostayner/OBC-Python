'''
* Avaliação e média de notas dos filmes

Desenvolva novas funcionalidades para complementar o nosso gerenciamento da classe Filmes. Segue o escopo das funcionalidades:

1 - Uma das funcionalidades requeridas é que o usuário possa realizar a avaliação de um filme passando uma nota como parâmetro e que essa nota seja salva no atributo específico da classe.

2 - Assim que uma avaliação for realizada, deve ser incrementado o total de avaliadores daquele filme. Obs: Considere criar um atributo específico para esse fim.

3 - Para cada filme ter uma nota de avaliação média consiste na divisão total de avaliação pelo total de avaliadores.
'''

class Movie:
    def __init__(self, name, lancamento, inclusoPlano, duracao,):
        self.name = name
        self.lancamento = lancamento
        self.inclusoPlano = inclusoPlano
        self.duracao = duracao
        self.totalAvaliacoes = 0
        self.avaliadores = 0


    def __str__(self):
        return f'Filme: {self.name}'
    
    def ficha_tecnica (self):
        print('Dados do Filme')
        print(f'Nome do Filme: {self.name}')
        print(f'Ano de Lançamento: {self.lancamento}')
        print(f'Está incluso no plano? {self.inclusoPlano}')
        print(f'Nº Avaliações {self.avaliadores}')
        print(f'Nota total: {self.totalAvaliacoes}')
        print(f'Duração: {self.duracao}')
    
    def avaliar (self, notas):
        self.totalAvaliacoes += notas
        self.avaliadores += 1

    def media (self):
        print(f'Média do filme {self.name} é {self.totalAvaliacoes / self.avaliadores}')

mario = Movie('Super Mario Bros', 2023, False, 130)
avatar = Movie('Avatar', 2023, False, 180)
mario.avaliar(10.0)
mario.avaliar(9.5)
avatar.avaliar(8.0)
avatar.avaliar(9.5)
avatar.avaliar(9.5)
mario.ficha_tecnica()
mario.media()
avatar.ficha_tecnica()
avatar.media()
