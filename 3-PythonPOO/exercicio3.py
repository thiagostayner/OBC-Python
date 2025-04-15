'''
Cadastro de Viagem

Desenvolva um mini cadastro de viagem que tenha os seguintes requisitos:

1 - Usuário deve informar o seu nome para cadastrar uma viagem.

2 - Usuário deve selecionar um destino com base nas instâncias de objetos da classe viagem.

3 - Deve ser apresentado uma mensagem indicando que o a cadastro da viagem no destino específico foi feito com sucesso.
'''

from exercicio3class import Viagem

viagem0 = Viagem('João Pessoa')
viagem1 = Viagem('Florianópolis')
viagem2 = Viagem('Gramado')
viagem3 = Viagem('Caldas Novas')
viagem4 = Viagem('Curitiba')

print('E ai viajante. Temos algumas ofertas para você.')
viajante = input('Digite o seu nome para começar: ')
print(f'{viajante} temos 5 destinos que combinam com voce'
    '''
    [0] - João Pessoa
    [1] - Florianópolis
    [2] - Gramado
    [3] - Caldas Novas
    [4] - Curitiba
    '''
    )

escolha = int(input('Selecione o destino da viagem: '))
list_viagens = [viagem0, viagem1, viagem2, viagem3, viagem4]

if escolha >= 5:
    print('Esta opção não é está inclusa nos destinos')
else:
    print(f'{viajante} sua viagem para {list_viagens[escolha].destino} está marcada')