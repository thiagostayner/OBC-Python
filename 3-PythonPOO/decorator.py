def my_decorator(func):
    def wrapper():
        print('Antes de executar a função')
        func()
        print('Depois de executar a função')
    return wrapper

def maiusculo_decorator(function):
    def wrapper ():
        func = function()
        maisculo = func.upper()
        return maisculo
    return wrapper

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper
