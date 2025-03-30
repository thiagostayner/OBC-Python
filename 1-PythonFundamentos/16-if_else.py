name = input('Digite o nome do jogo: ')
anoLancamento = int(input('Ano de lançamento do jogo: '))
classificacao = float(input('Digite a nota de classificação do jogo: '))

#uma das condições precisam ser verdadeiras
if classificacao > 8.0 or anoLancamento > 2015:
    print(f'O jogo {name} é bom. Recomendo jogá-lo')
else:
    print(f'O jogo {name} é ruim, não recomendo')

#ambas condições precisam ser verdadeiras
if classificacao > 8.0 and anoLancamento > 2015:
    print(f'O jogo {name} é bom. Recomendo jogá-lo')
else:
    print(f'O jogo {name} é ruim, não recomendo')