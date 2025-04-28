import os

def add_contact():
    name = input('Informe o nome: ')
    address = input('Informe o endereço: ')
    phone = input('Informe o fone: ')

    contact = f'Nome: {name} \nEnderço: {address} \nTelefone: {phone}\n'

    with open('4-ManipulandoArquivos/dados/contatos.txt', 'a', encoding='utf-8') as file:
        file.write(contact)

def view_contacts():
    if not os.path.exists('4-ManipulandoArquivos/dados/contatos.txt'):
        print('Lista de contatos está vazia')
        return
    with open ('4-ManipulandoArquivos/dados/contatos.txt', 'r', encoding='utf-8') as file:
        contacts = file.read()
        print('Lista de Contatos')
        print(contacts)

def delete_contacts():
    if not os.path.exists('4-ManipulandoArquivos/dados/contatos.txt'):
        print('Lista de contatos está vazia')
        return
    with open ('4-ManipulandoArquivos/dados/contatos.txt', 'w', encoding='utf-8') as file:
        file.write('')

    print('Contatos excluidos')