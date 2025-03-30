# 1 - Função para imprimir Hello World
def wellcome():
    print('Hello World')

wellcome()

# 2 - Função pra somar dois números
def soma():
    return 5 + 4
print(soma())

# 3 - Função para cadastrar um jogo:
def criar_jogo():
    name = str(input('Digite o nome do jogo: '))
    anoLancamento = int(input('Ano de lançamentos: '))
    preco = float(input('Valor do jogo: '))
    avaliacao = float(input('Digite a nota de avaliação do jogo: '))

    print(f'{name} - R$ {preco}')

criar_jogo()