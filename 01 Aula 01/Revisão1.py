import os
os.system('cls')

while True:

    while True:
        try: #TENTE FAZER ISSO:
            idade = int(input('Me informe sua idade por gentileza: '))
        except: #SE DER ERRADO:
            print('Digite apenas numneros')
        else: #SE DER CERTO
            break
                
    if idade < '12':
        print(f'Você tem {idade} e ainda é criança.')
    elif idade <= '17':
        print(f'Você tem {idade} e ja é adolescente.')
    elif idade <= '59':
        print(f'Você tem {idade} e ja pode ser preso.')
    else:
        print(f'Você tem {idade} e ja esta perto do fim KKKKKKKKKKKKKkKK.')

    while True:
        continuar = input('Deseja continuar? ').upper()
        if continuar not in 'SN': # SE NÃO FIZER PARTE DO QUE ESTA DENTRO DO PARENTESE FAÇA ISSO:
            print('Digite apenas S ou N')
        elif continuar == 'N':
            exit()
        elif continuar == 'S':
            break