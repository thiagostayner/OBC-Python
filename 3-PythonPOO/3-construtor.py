class Movie:
    def __init__(self, name, lancamento, inclusoPlano, nota, duracao): # método construtor
        self.name = name
        self.lancamento = lancamento
        self.inclusoPlano = inclusoPlano
        self.nota = nota
        self.duracao = duracao

    def __str__(self): #método para sobrescrever o objeto referenciado da classe
        return f'Filme: {self.name}'

filme = Movie('Super Mario Bros', 2023, False, 5.0, 130)
filme2 = Movie('Avatar', 2023, False, 4.0, 230)

print(filme.name)
print(filme2.name)

print(filme)
print(filme2)