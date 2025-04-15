class Animal:
    nome = ''
    tamanho = ''
    cor = ''

    def comer(self):
        print('Animal se alimentando')

class Cavalo(Animal):
    raca = ''

    def escapar(self):
        print('Cavalo fugindo')

class Leao(Animal):
    juba = True
    
    def cacar(self):
        print('Leão caçando')

c = Cavalo()
c.nome = "Carpeado"
c.cor = 'Branco'
c.escapar()
c.comer()

l = Leao()
l.nome = "Simba"
l.cor = 'marron'
l.cacar()
l.comer()