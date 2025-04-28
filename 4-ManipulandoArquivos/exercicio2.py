'''
Agenda de Contatos
- Desenvolva uma agenda de contatos persistindo as informações em arquivo.
O pragrama deve seguir as especificidades:
1 - Criar o arquivo Agenda contendo três métodos.
a. Um método para adicionar contato.
b. Um método para listar contatos.
c. Um método para remover contatos.
2 - Criar um arquivo principal para a aplicação que importar o módulo de agenda e chamar cada um dos métodos desenvolvidos de acordo com a opção escolhida.
'''

from agenda import add_contact, view_contacts, delete_contacts

def main():
    while True:
        print('Agenda de contatos')
        print('1 - Adiciona contato')
        print('2 - Listar contatos')
        print('3 - Remover contatos')
        print('4 - Sair')

        choice = input('Escolha a opção (1-4): ')

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            delete_contacts()
        elif choice == '4':
            break
        else:
            print('Opção inválida')

main()