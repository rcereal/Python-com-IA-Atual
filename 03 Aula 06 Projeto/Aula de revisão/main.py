# medias = []

# soma_notas = 0

# for pergunta in range(4):
#     nota = float(input('Digite a nota do aluno: '))
#     soma_notas += nota

# medias.append(soma_notas/4)

# for media in medias:
#     if media >= 7.0:
#         print('Aprovado')

#------------------------------------------------------------------

# idade = []
# altura = []

# for alturas in range (5):
#     pergunta1 = float(input('Digite a altura: '))
#     pergunta2 = input('Digite a idade: ')
#     idade.append(pergunta2)
#     altura.append(pergunta1)
    

# for i in range(len(idade)-1,-1,-1):
#     print(idade[i])

# for i in range(len(altura)-1,-1,-1):
#     print(altura[i])

#------------------------------------------------------------------

# dados = {
#     'nome': 'Pedro',
#     'idade': 25,
#     'sexo': 'M'
# }

# dados['idade']

# dados['pais'] = 'Brasil'

# del dados['sexo']

# dicionario = {
#     'nome': 'Jose',
#     'idade': 30,
#     'sexo': 'M',
#     'filhos': ['Joao', 'Maria', 'Pedro']
# }

# print(dicionario)
# ------------------------------------

# cachorros = {
#     'nome': [],
#     'raça': []
# }

# while True:
#     nome = input('Digite o nome do cachorro: ')
#     raça = input('Digite a raça do cachorro: ')
#     cachorros['nome'].append(nome)
#     cachorros['raça'].append(raça)
#     continuar = input('Deseja continuar? [S/N] ').upper()
#     if continuar == 'N':
#         break

# lista_de_nomes = cachorros['nome']
# lista_de_raças = cachorros['raça']

# for i in range(len(lista_de_nomes)):
#     print(f'{lista_de_nomes[i]} - {lista_de_raças[i]}')

# -----------------------------------------------

# função são blocos de codigos prontos
# que facilitam quando temos a necessidade 
# de aplicar codigos que precisam sempre5

# serem feitos a mão ou seja, quando criamos
# uma função basta apenas chama-la

#def nome_função(parametros):
    #codigo

def soma(primeiro_numero,segundo_numero):
    resultado = primeiro_numero + segundo_numero
    return resultado

numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite um numero: '))

print(soma(numero1,numero2))