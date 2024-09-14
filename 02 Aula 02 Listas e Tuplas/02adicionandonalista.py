# # .append PARA ADICIONAR O VALOR NA LISTA

# alunos = [True]
# while True:
#     aluno = input('Digite o nome do aluno: ')
#     if aluno == 'sair':
#         break
#     alunos.append(aluno) #SERVE PARA ADICIONAR O VALOR DO INPUT NA LISTA ALUNOS

# for aluno in alunos:
#     print(aluno)
# #--------------------------------------------------------------------------------------------

# # .insert PARA INSERIR VALOR NA LISTA

# lista = [True,False,False,True,False]

# lista.insert(3, 'infinity')

# print(lista)

# .remove PARA REMOVER O VALOR DA LISTA

alunos = []
while True:
    print('DESEJA ADICIONAR OU REMOVER UM ALUNO?')
    print('1 - ADICIONAR')
    print('2 - REMOVER')
    opcao = input('-> ')
    if opcao == '1':
        aluno = input('Digite o nome do aluno: ')
        if aluno == 'sair':
            break
        alunos.append(aluno)
        print(alunos)
    elif opcao == '2':
        aluno = input('Digite o nome do aluno que voce quer remover: ')
        alunos.remove(aluno)
        print(alunos)