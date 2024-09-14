from arquivoAnimal import  Animal

class Cachorro(Animal):
    def  __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca
    def som(self):
        return "Roof Roof"