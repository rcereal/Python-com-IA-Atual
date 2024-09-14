import os
os.system('cls')

lista_de_vezes = []

while True:
    while True:
        try: #TENTE FAZER ISSO:
            num1 = float(input('Informe um numero inteiro: '))
        except: #SE DER ERRADO:
            print('Digite apenas numeros')
        else: #SE DER CERTO
            break

    while True:
        try: #TENTE FAZER ISSO:
            num2 = float(input('Informe outro numero inteiro: '))
        except: #SE DER ERRADO:
            print('Digite apenas numeros')
        else: #SE DER CERTO
            break

    while True:
        try: #TENTE FAZER ISSO:
            num3 = float(input('Informe mais outro numero inteiro: '))
        except: #SE DER ERRADO:
            print('Digite apenas numeros')
        else: #SE DER CERTO
            break

    if num1 > num2 and num1 > num3:
        print(f'O primeiro numero, {num1} é maior que {num2} e {num3}')
    elif num2 > num1 and num2 > num3:
        print(f'O segundo numero, {num2} é maior que {num1} e {num3}')
    elif num3 > num1 and num3 > num2:
        print(f'O terceiro numero, {num3} é maior que {num1} e {num2}')

    while True:
        lista_de_vezes = input('Olá você deseja ver mais alguns numeros?: ').upper()
        if lista_de_vezes not in 'SN': # SE NÃO FIZER PARTE DO QUE ESTA DENTRO DO PARENTESE FAÇA ISSO:
            print('Digite apenas S ou N')
        elif lista_de_vezes == 'N':
            exit()
        elif lista_de_vezes == 'S':
            break
            
