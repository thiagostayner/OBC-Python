'''
Exercício Final:
* Gerenciamento de Jogadores e Times:
-> Escreva um programa em python que realize o gerenciamento de jogadores.
Ele deve atender aos seguintes requisitos:
1 - A opção de listar os times deve mostrar o indice, o nome e a quantidade de jogadores do time.
2 - A opção de adicionar um time deve pedir um nome para o time que será cadastrado.
3 - A opção de remover um time deve pedir o índice específico do time que foi cadastrado para fazer a sua exclusão.
4 - A opção de adicionar um jogador em um time deve pedir o índice do time que foi cadastrado e associar com o nome do time que será adicionado.
5 - A opção de remover um jogador em um time deve pedir um índice do time que foi cadastrado e utilizar esse índice para remover o jogador que fora cadastrado no time.
6 - A opção de listar os jogadores de um time deve ser informado o índice de um time e listar os jogadores que foram associados a ele.

obs: Este é o exercício de final do módulo, então aproveita para utilizar todos os recursos vistos até agora, como funções, condições, loop, listas, etc.
'''

times = {}
controle = False

# função para listar times
def print_teams():
    print('Times listados:')
    for i, time in enumerate(times.values()):
        print(f'{i+1}. {time["name"]} ({len(time["players"])}) jogadores')

# função para listar jogadores de um time
def print_jogadores(time):
    print(f'Jogadores do {time["name"]}')
    for i, player in enumerate(time["players"]):
        print(f'{i+1}. {player}')

while not controle:
    # Opções no programa
    print('1. Adicionar um time')
    print('2. Remover um time')
    print('3. Listar times')
    print('4. Adicionar jogador em um time')
    print('5. Remover jogador em um time')
    print('6. Listar jogadores de um time')
    print('7. Sair')

    escolha = input ('>')

    if escolha == '1':
        nome_time = input('Digite o nome do time: ')
        times[nome_time] = {'name' : nome_time, 'players' : []}
        print('Time adicionado')
    elif escolha == '2':
        print_teams()

        num_time = int(input('Informe o número do time que deseja remover: '))
        if num_time <= len(times):
            nome_time = list(times.keys())[num_time - 1]
            del times[nome_time]
            print('Time removido')
        else:
            print('Número inválido')
    elif escolha == '3':
        print_teams()
    elif escolha == '4':
        print_teams()

        num_time = int(input('Informe o número do time que deseja adicionar o jogador: '))
        if num_time <= len(times):
            nome_time = list(times.keys())[num_time - 1]
            nome_jogador = input('Informe o nome do jogador: ')
            times[nome_time]['players'].append(nome_jogador)

    elif escolha == '5':
        print_teams()
        num_time = int(input('Informe o número do time que deseja remover os jogadores: '))
        if num_time <= len (times):
            nome_time = list(times.keys())[num_time - 1]
            print_jogadores(times[nome_time])
            num_player = int(input('Informe o número do jogador que deseja remover: '))
            if num_player <= len(times[nome_time]['players']):
                del times[nome_time]['players'][num_player - 1]
                print('Jogador removido')
            else:
                print('Número do jogador inválido')
        else:
            print('Número do time inválido.')
    elif escolha == '6':
        print_teams()
        num_time = int(input('Informe o número do time que deseja ver os jogadores: '))
        if num_time <= len (times):
            nome_time = list(times.keys())[num_time - 1]
            print_jogadores(times[nome_time])
        else:
            print('Número do time inválido')
    elif escolha == '7':
        controle = True
    else:
        print('Opção inválida')
