# COLEÇÃO

# -> LISTAS
# SAO MUTAVEIS E INDEXAVEIS
# MUTAVEIS = os valores que possuem dentro da lista podem ser alterados, adicionados ou excluidos
# INDEXAVEIS = os valores que possuem dentro da lista podem ser acessados por um indice
# Para declarar uma lista utiliza-se [ ]
# exemplo:
lista_de_nomes = ['Guilherme', 150, 1.84, True]

# SEMPRE QUE FOR ACESSAR UM VALOR DENTRO DE UMA COLECAO UTILIZA-SE []
# print(lista_de_nomes[0])
# E PARA MODIFICAR UTILIZA-SE O NOME DA LISTA E A POSIÇÃO DO VALOR
lista_de_nomes[0] = 'Joaquim'

# METODOS
# METODOS ACOES QUE IRÃO RETORNAR OU MANIPULAR ALGO DA COLEÇÃO
# COMO UTILIZA-SE METODO ?
# nome_coleção.nome_do_metodo(parametro)
# exemplo
lista_de_nomes.append('ryan')

# Metodos para -->ADICIONAR<-- valores
# - append() -> adiciona um valor no final da lista
# - insert() -> adiciona um valor em uma posicao especifica

# metodos para -->REMOVER<-- valores
# - pop() -> remove o valor final da lista
# - remove() -> remove um valor especifico da lista

# metodos para -->ALTERAR<-- valores
# - sort() -> ordena a lista
# - reverse() -> inverte a ordem da lista

#-------------------------------------------------------------------------------------------------------

# ->TUPLAS
# MUTAVEIS = os valores que possuem dentro da lista NÃO podem ser alterados, adicionados ou excluidos
# INDEXAVEIS = os valores que possuem dentro da lista podem ser acessados por um indice
# Para declarar uma TUPLA utiliza-se ( )
# exemplo:
tupla_de_nomes = ('Guilherme', 150, 1.84, True)

# É POSSIVEL ACESSAR OS VALORES DENTRO DE UMA TUPLA MAS NÃO É POSSIVEL ALTERA-LOS
print(tupla_de_nomes[2])

# METODOS
# print(tupla_de_nomes.count('Guilherme')) retorna quantos valores iguais tem na tupla_
# print(tupla_de_nomes.index('Guilherme')) retorna o valor da posição escolhida


# ->DICIONARIOS
# NÃO INDEXADOS E MUTAVEIS
# NÃO INDEXADO = os valores são acompanhados por chaves sendo assim não possuem uma posição especifica
# MUTAVEIS = os valores que possuem dentro da lista podem ser alterados, adicionados ou excluidos
# as chaves e os valores do dicionario podem ser qualquer tipo de dado(string, float, int,bool)
# exemplo:

# dicionario_de_nomes = {'nome': 'Guilherme',
#                        'idade': 150,
#                        'altura': 1.84,
#                        'peso': True}
# ACESSANDO UM VALOR DO DICIONARIO
# print(dicionario_de_nomes['nome'])

# OS VALORES DO DICIONARIO PODE SER ALTERADOS
# dicionario_de_nomes['nome'] = 'Joaquim'

#METODOS
# ADICIONA UMA NOVA CHAVE E VALOR NO DICIONARIO
# dicionario_de_nomes.update({'chave adicionada pelo update':'valor adicionado pelo update'})
# print(dicionario_de_nomes)

# limpa o dicionario deixando totalmente vazio
# dicionario_de_nomes.clear()


#