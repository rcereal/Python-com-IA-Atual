from arquivoAnimal import  Animal

class Gato(Animal):
    def __init__(self, nome, idade, cor):
        super().__init__(nome, idade)
        self.cor = cor
    def som(self):
        return "Meowwwwh"

