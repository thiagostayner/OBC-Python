'''
O Jogo dos Dados Mágicos 🎲✨
No reino encantado de Pythonlandia, existe um jogo muito antigo que os feiticeiros jogam para determinar quem terá a honra de liderar o conselho mágico. O jogo envolve lançar dados mágicos, mas esses dados são diferentes, eles têm poderes especiais! 🧙‍♂️🔮

Cada dado mágico possui o encantamento que faz com que o valor observe a seguinte regra: se o valor do dado for múltiplo de 3, ele se transforma em 'Fizz', se for múltiplo de 5, ele vira 'Buzz'. Se o valor for múltiplo de ambos, ele vira 'FizzBuzz'. Caso não seja múltiplo de nenhum, permanece o número original.

O conselho mágico pede a sua ajuda para criar um feitiço (código) que receba como entrada uma lista de valores de dados lançados e retorne uma nova lista convertida com base na regra mágica.
'''

dados = [2, 4, 6, 9, 10, 30]
dados_magicos = []

for i in dados:
    if i % 3 == 0 and i % 5 == 0:
        dados_magicos.append('FizzBuzz')
    elif i % 5 == 0:
        dados_magicos.append('Buzz')
    elif i % 3 == 0:
        dados_magicos.append('Fizz')
    else:
        dados_magicos.append(i)

print(dados_magicos)