class Pai:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

class Filha(Pai):
    def __init__(self, nome, idade, altura):
        super().__init__(nome, idade)
        
        self.altura = altura

    def aniversario(self):
        self.idade += 2

class Bebe(Filha):
    def __init__(self, nome, idade, altura):
        super().__init__(nome, idade, altura)


objeto_filha = Filha('Gabriela', 20, 1.60)

objeto_bebe = Bebe('Diego', 1, 1.1)

print(objeto_filha.__dict__)
print(objeto_bebe.__dict__)