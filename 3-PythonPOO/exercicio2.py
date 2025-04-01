'''
* Classe Produto e método desconto
Desenvolva uma classe em Python pra atender as seguintes especificadades de um Produto:

1 - Cada produto deve ter um preço e um nome.

2 - A classe deve ter um método construtor e o método dundle str.

3 - A classe deve ter um método para desconto.
O método deve receber o desconto em percentual e realizar o cálculo de quanto fica o preço final com o desconto
'''

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def __str__(self):
        return f'Produto: {self.nome} - R$ {self.preco}'
    
    def resumo (self):
        print(f'Produto: {self.nome}')
        print(f'Preço: R$ {self.preco:.2f}')
    
    def promocao (self, desconto):
        self.desconto = desconto
        print(f'Você obteve um desconto de {self.desconto}%.')
        print(f'Valor final do produto é de R$ {self.preco - (self.preco * self.desconto) / 100:.2f}')
        
computador = Produto('Computador', 4500.00)
computador.resumo()
computador.promocao(10)
iphone = Produto('Iphone', 7500)
iphone.resumo()
iphone.promocao(15)