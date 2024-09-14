from poo import Aluno


pergunta_nome = input('Digite seu nome: ')
pergunta_idade = int(input('Digite sua idade: '))
pergunta_curso = input('Digite seu curso: ')

primeiro_aluno = Aluno(pergunta_nome, pergunta_idade, pergunta_curso)

primeiro_aluno.envelhecer(30)

print(primeiro_aluno.__dict__)