
email = ('ryanvitor@gmail.com')
senha = ('123')
usuarios = []

while True:
    pergunta_email = input('Digite seu email: ')
    pergunta_senha = input('Digite sua senha: ')

    if pergunta_email == email and pergunta_senha == senha:
        print('OLÁ MESSIAS DA MARVEL! BEM VINDO AO SEU BANCO DE INFORMAÇÕES DE USUARIOS CADASTRADOS.')
        break
    else:
        print('Email ou senha incorretos. Tente novamente!')

print(' ')
print('MENU DE COMANDOS:')

def remover(lista_usuario,nome_do_usuario):

    for usuario in lista_usuario:
        if nome_do_usuario == usuario['nome']:
            lista_usuario.remove(usuario)


while True:
    print('1 - Cadastrar')
    print('2 - Remover')
    print('3 - Sair')

    opcao = int(input('Digite a opção que deseja.(1/2/3)'))

    if opcao == 1:
        while True:
            nome_usuario = input('Digite o nome: ')
            idade_usuario = int(input('Digite a idade: '))
            altura_usuario = float(input('Digite a altura: '))
            peso_usuario = float(input('Digite o peso: '))
            informacoes = {
                'nome' : nome_usuario,
                'idade' : idade_usuario,
                'altura' : altura_usuario,
                'peso' : peso_usuario
            } 
            usuarios.append(informacoes)
            continuar = input('Deseja cadastrar outro usuario? [S/N] ').upper()
            if continuar == 'N':
                break
            print(informacoes)
    elif opcao == 2:
        print(usuarios)
        nome_usuario = input('Digite o nome do usuario que deseja remover: ')    
        remover(usuarios,nome_usuario)
        print(usuarios)
    elif opcao == 3:
        print('Obrigado por usar o nosso sistema!')
        break
    
    









