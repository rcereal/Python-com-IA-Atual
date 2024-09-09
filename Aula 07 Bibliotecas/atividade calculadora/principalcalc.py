import funcoescalc

email = ('123')
senha = ('123')

while True:
    pergunta_email = input('Digite seu email: ')
    pergunta_senha = input('Digite sua senha: ')

    if pergunta_email == email and pergunta_senha == senha:
        print('OLÁ MESSIAS DA MARVEL! BEM VINDO A SUA CALCULADORA.')
        break
    else:
        print('Email ou senha incorretos. Tente novamente!')

print(' ')
print('MENU DE COMANDOS:')


while True:
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')

    opcao = int(input('Digite a opção que deseja (1/2/3/4): '))

    primeiro_numero = float(input('Digite o primeiro numero: '))
    segundo_numero = float(input('Digite o segundo numero: '))

    if opcao == 1:
        print(funcoescalc.soma(primeiro_numero,segundo_numero))
        continuar = input('Deseja fazer outro calculo? [S/N] ').upper()
        if continuar == 'N':
            break
    
    elif opcao == 2:
        print(funcoescalc.subtracao(primeiro_numero,segundo_numero))   
        continuar = input('Deseja fazer outro calculo? [S/N] ').upper()
        if continuar == 'N':
            break

    elif opcao == 3:
        print(funcoescalc.multiplicacao(primeiro_numero,segundo_numero))
        continuar = input('Deseja fazer outro calculo? [S/N] ').upper()
        if continuar == 'N':
            break
    
    elif opcao == 4:
        print(funcoescalc.divisao(primeiro_numero,segundo_numero))
        continuar = input('Deseja fazer outro calculo? [S/N] ').upper()
        if continuar == 'N':
            break