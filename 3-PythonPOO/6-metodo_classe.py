'''
1 - O método de classe utiliza o parâmetro referente a classe.
2 - O método de classe pode acessar ou modificar o estado da classe.
3 - Usamos o decorator @classmethod para criar o método de classe
'''

class Console:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    @classmethod
    def from_text (cls, string):
        import re
        item = re.findall('é \w*', string)
        nome = item[0][2:]
        preco = item[1][2:]
        return cls(nome, int(preco))
    
wiiU = Console.from_text('Meu video game é WiiU e o preço é 1000 reais')
xboxOne = Console.from_text('Meu video game é XboxOne e o preço é 1500 reais')
print(wiiU.__dict__)
print(xboxOne.__dict__)