import os
os.system ('cls')

idades = []

while True:
    while True:
        try: #TENTE FAZER ISSO:
            numeroP = int(input('Quantas pessoas deseja cadastrar? '))
        except: #SE DER ERRADO:
            print('Digite apenas numeros')
        else: #SE DER CERTO
            break

    soma_idades = 0
    
    for i in range (numeroP):
        idade = int(input(f"Digite a idade da pessoa {i+1}: "))
        idades.append(idades)
        soma_idades += idade

    media = soma_idades / numeroP

    if media > 0 and media <= 25:
        print(f'A média da sala é {media:.2f} e o grupo é considerado Jovem')
    elif media >= 26 and media <= 60:
        print(f'A média da sala é {media:.2f} e o grupo é considerado Adulto')
    elif media > 60:
        print(f'A média da sala é {media:.2f} e o grupo é considerado Idoso')
    
    while True:
        continuar = input('Olá você deseja continuar? ').upper()
        if continuar not in 'SN':
            print('Digite apenas S ou N')
        elif continuar == 'N':
            exit()
        elif continuar == 'S':
            break