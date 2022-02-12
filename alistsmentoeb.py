from datetime import date

# Cabeçalho do Sistema
print('=== \033[1;37mAlistamento\033[m \033[1;4;32;40mExército Brasileiro\033[m ===')
print('')
atual = date.today().year
print('\033[1;37;40m--- Registro ---\033[m')
print('')
ano = int(input('Ano de nascimento: '))
idade = atual - ano

class Menu():
    sexo = int(input('''
\033[1;37;40m--- Escolha o seu sexo ---\033[m
   
[1] \033[1;34mHomem\033[m
[2] \033[1;35mMulher\033[m

Escolha uma opção: '''))
    if sexo == 1:
        print('')
        print('\033[1;37;40m--- Servidor ---\033[m')
        print('')
        print('> \033[1;37mStatus:\033[m \033[1;32mAlistamento Obrigatório.\033[m')
    elif sexo == 2:
          print('')
          print('\033[1;37;40m--- Servidor ---\033[m')
          print('')
          print('> \033[1;37mStatus:\033[m \033[1;31mVocê não precisa se alistar.\033[m')
    else:
        print('\033[1;31mError\033[m: \033[4;1;37mSó existe apenas duas opções.\nTente novamente.\033[m')

class Alistamento():
    print('')
    print('\033[1;37;40m--- Sistema \033[1;32mE.B \033[1;37;40m---\033[m')
    print('')
    if idade == 18:
        print('\033[1;30m> Quem nasceu no ano de {} tem {} ano(s)\nem {}.\033[m'.format(ano,idade, atual))
    elif ano > date.today().year:
        print('\033[1;36m> MEU DEUS!!! VOCÊ VEIO DO FUTURO??? :o\033[m')
    elif idade < 18:
        anos = 18 - idade
        print('\033[1;30m> Quem nasceu no ano de \033[1;37m{}\033[m \033[1;30mtem\033[m \033[1;37m{} ano(s)\033[m\n\033[1;30mem\033[m \033[1;37m{}\033[m.\033[m'.format(ano,idade, atual))
        print('')
        print('\033[1;33;40m--- AVISO DO SISTEMA ---\033[m')
        print('')
        print('\033[1;30m> Você ainda não tem idade para se alistar.\n Ainda faltam \033[1;37m{}\033[m \033[1;37mano(s)\033[m \033[1;30mpara o alistamento\033[m.\033[m'.format(anos))
    elif idade > 18:
        anos = idade - 18
        print('\033[1;30m> Quem nasceu no ano de \033[1;37m{}\033[m \033[1;30mtem\033[m \033[1;37m{} ano(s)\033[m\n\033[1;30mem\033[m \033[1;37m{}.\033[m'.format(ano,idade, atual))
        print('')
        print('\033[1;31;40m--- AVISO DO SISTEMA ---\033[m')
        print('')
        print('\033[1;30m> Você já deveria-se alistar há \033[1;37m{} ano(s)\033[m \033[1;30matrás\033[m!!'.format(anos))
