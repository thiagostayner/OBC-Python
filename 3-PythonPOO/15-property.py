class Person:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome (self, value):
        if not isinstance(value, str):
            raise TypeError("Nome deve ser uma string")
        self._nome = value

        
pessoa = Person("fulano", 12)
print(vars(pessoa))