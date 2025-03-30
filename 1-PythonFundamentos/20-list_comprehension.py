# 1 - liste valores de 0 a 10 que sejam menor do que 4.

# for i in range(10):
#     if i < 4:
#         print(i)

listaNumeros = [i for i in range(10) if i < 4]
print(listaNumeros)

listaJogos = ["Mario Odyssey", 'DK Country', 'Luigis Mansion', 'Kirby']

# 2 - Jogos que poussuam a letra a
novaLista = [x for x in listaJogos if 'a' in x]
print(novaLista)

for x in listaJogos:
    if 'a' in x:
        print(x)

# 3 - Jogos que eu zerei
jogosZerados = [x for x in listaJogos if x != 'Kirby']
print(jogosZerados)

for x in listaJogos:
    if x != 'Kirby':
        print(x)