'''
1 - O método estático não utiliza o parâmetro referente a classe.
2 - O método estático pode acessar mas não pode modificar o estado da classe.
3 - Usamos o decorator @staticmethod para criar um método estático
'''

class Curso:
    def __init__(self, nome, trilha):
        self.nome = nome
        self.trilha = trilha

    @staticmethod
    def trilha_cursos(trilha):
        if trilha == 'Python Fundamentos':
            cursos = ['Dominando Python', 'Módulos e Pip', 'Orientação a Objetos']
        elif trilha == 'Automação com o Python':
            cursos = ['Automação de Tarefas', 'Web Scraping', 'Assistente Virtual em Python']
        else:
            cursos = ['A definir']
        return cursos

print(Curso.trilha_cursos('Python Fundamentos'))
print(Curso.trilha_cursos('Automação com o Python'))
print(Curso.trilha_cursos('Análise de Dados'))
