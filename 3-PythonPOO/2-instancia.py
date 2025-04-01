class Movie:
    name = ''
    lancamento = 0
    inclusoPlano = False
    nota = 0
    duracao = 0

# Primeiro Filme
filme = Movie()
filme.name = 'Super Mario Bros'
filme.lancamento = 2023
filme.inclusoPlano = False
filme.nota = 5.0
filme.duracao = 130

# Segundo Filme
deadpool3 = Movie()
deadpool3.name = 'Deadepool & Wolverine'
deadpool3.lancamento = 2024
deadpool3.inclusoPlano = False
deadpool3.nota = 5.0
deadpool3.duracao = 128

print('Dados do Filme')
print(f'Nome do filme {filme.name}\nAno de lançamento: {filme.lancamento}')