# Atividade: Sistema de Cadastro de Estudantes e Cursos

# Você está desenvolvendo um sistema simples para gerenciar estudantes e cursos em uma escola. 
# O sistema deve permitir associar estudantes aos cursos que eles estão matriculados.

# Instruções:

# Definição de Classes:

# Crie uma classe chamada Estudante com os atributos nome e id_estudante.
class Estudante:
    def __init__(self,id,nome):
        self.id = id
        self.nome = nome
        self.cursos = []
# Crie uma classe chamada Curso com os atributos nome e codigo_curso.

class Curso:
    def __init__(self,nome, codigo_curso):
        self.nome = nome
        self.codigo_curso = codigo_curso
        self.estudantes = []

# Associação:
# Adicione um atributo à classe Estudante para armazenar uma lista de cursos aos quais o estudante está matriculado.
# Adicione um atributo à classe Curso para armazenar uma lista de estudantes matriculados no curso.


while True:
    print('cadastrar(1) sair(2)')

    escolha = input('Digite uma opção: ')

    if escolha == '1':
        nome_do_curso = input('Digite o nome do curso')
        codigo_do_curso = int(input('Digite o codigo do curso'))

        objeto_Curso = Curso(nome_do_curso, codigo_do_curso)

        id_estudante = input('Digite o id do Estudante: ')
        nome_estudante = input('Digite o nome do Estudante: ')

        objetoEstudante = Estudante(id_estudante,nome_estudante)

        objeto_Curso.estudantes.append(objetoEstudante.nome)

        objetoEstudante.cursos.append(objeto_Curso.nome)


        print(objeto_Curso.__dict__)
        print(objetoEstudante.__dict__)

