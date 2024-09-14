class Pai:
    def __init__(self,nome,idade) :
        self.nome = nome
        
        self.idade = idade

        self.dedos_da_mao = 10
    
    def aniversario(self):
        self.idade += 1

#A classe Filha esta herdando os atributos e os metodos da classe Pai, por exemplo, os atributos de  nome, idade e dedos_da_mao ja serao inlcuidos na classe filha
class Filha(Pai):
    def __init__(self, nome, idade,altura):
        super().__init__(nome, idade)

        self.altura = altura


class Bebe(Filha):
    def __init__(self, nome, idade,altura):
        super().__init__(nome, idade,altura)




objetoPai = Pai('Claudio',40)

objetoFilha = Filha('Amanda',12, 1.50)

objetoPai.aniversario()
print(objetoPai.__dict__)

objetoFilha.aniversario()
print(objetoFilha.__dict__)

