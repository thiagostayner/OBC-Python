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

times = {'Flamengo' : ['Arrascaeta', 'BH27', 'Wesley'], 'Corinthians' : ['Garro', 'Memphis', 'Yuri Alberto'], 'São Paulo' : []}
continua = True

def listarTimes ():
    for i, (k, v) in enumerate(times.items()):
        print(f'[{i}] - {k} possui {len(v)} jogadores')


while continua == True:
    print('=' * 40)
    print('1 - Mostra elenco')
    print('2 - Adicionar elenco')
    print('3 - Remover elenco')
    print('4 - Adicionar jogador a um elenco')
    print('5 - Remover jogador de um elenco')
    print('6 - Listar jogadores de um elenco')
    print('7 - Sair')
    print('=' * 40)
    escolha = int(input('Qual opção deseja acessar? '))

    if escolha == 1:
        listarTimes()
    if escolha == 2:
        addTime = str(input('Qual o nome do time que deseja adicionar? '))
        times[addTime] = []
    if escolha == 3:
        listarTimes()

        excluirTime = int(input('Informe o índice do time que deseja excluir: '))
        chaveTimes = list(times.keys())
        if 0 <= excluirTime < len(chaveTimes):
            timeRemovido = chaveTimes[excluirTime]
            times.pop(timeRemovido)
        else:
            print('Índice inválido')
    if escolha == 4:
        listarTimes()

        indiceTime = int(input('Informe o time que deseja adicionar o jogador: '))
        addJogador = str(input('Informe o nome do jogador: '))
        chaveTimes = list(times.keys())
        if 0 <= indiceTime < len(chaveTimes):
            timeEscolhido = chaveTimes[indiceTime]
            times[timeEscolhido].append(addJogador)
        else:
            print('Índice inválido')
    if escolha == 5:
        listarTimes()

        indiceTime = int(input('Informe o indice do time que deseja remover um jogador: '))
        chaveTimes = list(times.keys())
        if 0 <= indiceTime < len(chaveTimes):
            timeEscolhido = chaveTimes[indiceTime]
            jogadores = times[timeEscolhido]

            if not jogadores:
                print(f'O time {timeEscolhido} não tem jogadores para remover')
                continue
            
            print(f'Jogadores do {timeEscolhido}')
            for i, jogador in enumerate(jogadores):
                print(f'[{i}] - {jogador}')
            indiceJogador = int(input('Qual o indice do jogador que deseja remover: '))
            if 0 <= indiceJogador < len(jogadores):
                jogadores.pop(indiceJogador)
                print('Jogador excluido.')
            else:
                print('Índice inválido.')
        else:
            print('Indice inválido')
                
    if escolha == 6:
        listarTimes()

        indiceTime = int(input('Informe o indice do time que deseja listar: '))
        chaveTimes = list(times.keys())
        if 0 <= indiceTime < len(chaveTimes):
            timeEscolhido = chaveTimes[indiceTime]
            jogadores = times[timeEscolhido]

            if not jogadores:
                print(f'O time {timeEscolhido} não tem jogadores para listar')
                continue
            print(f'Jogadores do time {timeEscolhido} escolhido: ')
            for i, jogador in enumerate(jogadores):
                print(f'[{i}] - {jogador}')
        else:
            print('Indice do time não confere')
    if escolha == 7:
        print('Sistema encerrado')
        continua = False
