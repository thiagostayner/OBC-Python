'''
* Agendamento de desligamento PC
=> Crie duas funções em python para agendar o desligamento do computador em uma hora e meia hora
'''

import os

# desligar na hora
def desl_agora():
    return os.system('shutdown /s /t 0')

# desligar em 1 minuto
def desl_1min():
    return os.system('shutdown /s')

# desliga em 30 minutos
def desl_30min():
    return os.system('shutdown /s /t 1800"')

# desliga em 1 hora
def desl_1hr():
    return os.system('shutdown /s /t 3600"')

# aborta o cancelamento
def cancel_desl():
    return os.system('shutdown /a')