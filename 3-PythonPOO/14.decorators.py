from decorator import my_decorator, maiusculo_decorator, split_string

# Exemplo 1
@my_decorator
def my_function():
    print('Dentro da função')

my_function()

# Exemplo 2
@maiusculo_decorator
def text():
    return "Hello Word"

print(text())

# Exemplo 3
@split_string
@maiusculo_decorator
def example():
    return "Aprendendo Python e criando decorators"

print(example())