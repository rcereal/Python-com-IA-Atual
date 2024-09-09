import funcoesA8

# ATIVIDADE 1: Dada uma lista de numeros, crie uma nova lista contendo apenas os numeros pares

# lista_de_pares = []

# for i in range(0,3):
#    valores = int(input('Digite um numero: '))
#    if valores % 2 == 0:
#      lista_de_pares.append(valores)

# print(lista_de_pares)

# ATIVIDADE 2: Crie um dicionário com informações de produtos,
# incluindo nome, preço e quantidade em estoque. Implemente funções
# para adicionar, remover e atualizar produtos no dicionário.

# print('Bem Vindo ao estoque da FutSports.')
# print('----------------------------------')

# dicionario_de_produtos = {
#     'Nome': [],
#     'Preco': [],
#     'Quantidade': []
# }

# while True:
#     print(dicionario_de_produtos)
#     print('1 - Adicionar')
#     print('2 - Remover')
#     print('3 - Atualizar')

#     opcao = int(input('Digite a opção que deseja (1/2/3): '))

#     if opcao == 1:
#         dicionario_de_produtos['Nome'].append(input('Nome: '))
#         dicionario_de_produtos['Preco'].append(float(input('Preco: ')))
#         dicionario_de_produtos['Quantidade'].append(int(input('Quantidade: ')))

#         continuar = input('Deseja fazer outra opção? [S/N] ').upper()
#         if continuar == 'N':
#             print(dicionario_de_produtos)
#             break

#     elif opcao == 2:
#         print(dicionario_de_produtos)

#         posicao_produto = int(input('Digite a posição do produto no qual você deseja remover: '))

#         dicionario_de_produtos['Nome'].pop(posicao_produto)
#         dicionario_de_produtos['Preco'].pop(posicao_produto)
#         dicionario_de_produtos['Quantidade'].pop(posicao_produto)

#         continuar = input('Deseja fazer outra opção? [S/N] ').upper()
#         if continuar == 'N':
#             print(dicionario_de_produtos)
#             break
#     elif opcao == 3:
#         nome_produto = str(input('Digite o nome do produto que deseja atualizar: '))
#         posicao_produto = dicionario_de_produtos['Nome'].index(nome_produto)
        
#         novo_nome_produto = str(input('Digite o novo nome do produto: '))
#         dicionario_de_produtos['Nome'][posicao_produto] = novo_nome_produto

#         novo_preco_produto = float(input('Digite o novo preco do produto: '))
#         dicionario_de_produtos['Preco'][posicao_produto] = novo_preco_produto

#         nova_quantidade_produto = int(input('Digite a nova quantidade do produto: '))
#         dicionario_de_produtos['Quantidade'][posicao_produto] = nova_quantidade_produto

#         continuar = input('Deseja fazer outra opção? [S/N] ').upper()
#         if continuar == 'N':
#             print(dicionario_de_produtos)
#             break
#     else:
#         print('Opção inválida. Tente novamente!')
#         continue

# ATIVIDADE 3: Crie um conjunto com nomes de cores. Implemente
# uma função que retorne as cores que têm mais de quatro letras.


cores = ['Vermelho', 'Azul', 'Verde', 'Amarelo']

print(funcoesA8.contador_letras(cores))
