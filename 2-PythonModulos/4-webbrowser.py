import webbrowser

done = False

while not done:
    print('O que deseja fazer?\n1. Aprender Python\n2. Aprender sobre módulos\n3. Aprender Python, Fullstack JS, Inglês e No Code\n4.Sair')

    escolha = input('>')

    if escolha == '1':
        webbrowser.open('http://www.python.org')
    elif escolha == '2':
        webbrowser.open('https:docs.python.org/3/py-modindex.html')
    elif escolha == '3':
        webbrowser.open('https://onebitcode.com')
    elif escolha == '4':
        done = True
    else:
        print('Opção inválida, escolha uma opção entre 1 a 4')