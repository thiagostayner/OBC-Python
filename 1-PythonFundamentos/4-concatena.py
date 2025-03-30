nome = str(input('Digite o nome do jogo: '))
anoLancamento = int(input('Digite o ano de lançamento do jogo: '))
preco = float(input('Digite o valor do jogo: '))
planIncluded = input('Está incluso no serviço mensal? ')

print('###Dados do Jogo###')
print('='*20)
print(f'Nome do jogo {nome} \nAno de lançamento {anoLancamento} \nPreço do jogo {preco:.2f}\nEstá em uma biblioteca mensal? {planIncluded}')
