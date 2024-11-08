from time import sleep

c = ('\033[m',       # Sem cores
     '\033[0;30;41m',# Vermelho
     '\033[0;30;42m',#verde
     '\033[0;30;43m',#amarelo
     '\033[0;30;44m',#azul
     '\033[0;30;45m',#roxo
     '\033[1;107m',   #branco
    )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    print(c[cor], end='')
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)



# Programa principal
comando = ''
while True:
    titulo('Sistema de ajuda Pyhelp', 2)
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo', 1)