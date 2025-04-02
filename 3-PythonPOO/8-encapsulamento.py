class Employee:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario # não permite acesso usando dois underline

    def show(self):
        print(f'Nome {self.nome} - Salário {self.__salario}')

fulano = Employee('Fulano', 4000)
siclano = Employee('Siclano', 5000)
fulano.show()
siclano.show()
fulano.__salario = 40000
fulano.show()