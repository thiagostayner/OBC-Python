class Movie:
    def __init__(self, name, lancamento, inclusoPlano, nota, duracao):
        self.name = name
        self.lancamento = lancamento
        self.inclusoPlano = inclusoPlano
        self.nota = nota
        self.duracao = duracao

    def __str__(self):
        return f'Filme: {self.name}'
        
    def ficha_tecnica(self):
        print('=========Dados do Filme=========')
        print(f'Nome do Filme: {self.name}')
        print(f'Lançamento: {self.lancamento}')
        print(f'O filme está no plano? {self.inclusoPlano}')
        print(f'Avaliação do filme: {self.nota}')
        print(f'Duração do filme: {self.duracao}\n')

mario = Movie('Super Mario Bros', 2023, False, 5.0, 130)
top_gun = Movie('Top Gun Maverick', 2022, True, 4.5, 160)

mario.ficha_tecnica()
top_gun.ficha_tecnica()