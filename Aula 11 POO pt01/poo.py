#POO 
#PROGRAMAÇÃO ORIENTADA A OBJETO
# É UMA FORMA DE ESTRUTURAR MELHOR O SISTEMA A SER DESENVOLVIDO

#-----------------------------------------------------------------------------

#CLASSE
#Classe é um molde de algo do mundo real
#Exemplo: Aluno, Cachorro, Pessoa
# o que todo aluno tem ?
#ATRIBUTOS, OU SEJA, as caracteristicas da classe: nome, idade, curso

#-----------------------------------------------------------------------------

#METODOS
#Metodos são ações que a classe vai executar podendo manipular
#um atributo/estado da classe

#-----------------------------------------------------------------------------

#class Nome_da_classe
#OBS: TODA CLASSE CRIADA DEVE SER INICIADA COM LETRA MAISCULA
#E O RESTANTE MINUSCULA
class Aluno:
    #METODO CONSTRUTOR
    #é no metodo construtor que definimos os atributos da nossa classe
    def __init__(self,nome:str ,idade:int, curso:str):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def envelhecer(self,valor_a_ser_passado_para_envelhecer_objeto):
        self.idade += valor_a_ser_passado_para_envelhecer_objeto
        return self.idade

#OBJETO
#objetos são uma instancia de uma classe, ou seja, são algo pertencentes
#a classe

