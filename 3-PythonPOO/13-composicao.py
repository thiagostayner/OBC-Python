class Animal:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria

class Peixe(Animal):
    raca = ''

class Papagaio(Animal):
    cor = ''

class Zoo:
    def __init__(self):
        self.animals_dict = {}

    def add_animal(self, animal):
        self.animals_dict[animal.nome] = animal.categoria

    def total_de_categorias(self, categoria):
        result = 0
        for animal in self.animals_dict.values():
            if animal == categoria:
                result += 1

        return f'No nosso zoológico temos {result} quanitade de {categoria}'
    
zoo = Zoo()
peixe = Peixe('Nemo', 'mamíferos')
peixe2 = Peixe('Fulano', 'mamíferos')
print(vars(peixe))

papagaio = Papagaio('Louro', 'aves')
print(vars(papagaio))

zoo.add_animal(peixe)
zoo.add_animal(papagaio)
zoo.add_animal(peixe2)
print(zoo.total_de_categorias('aves'))
print(zoo.total_de_categorias('mamíferos'))