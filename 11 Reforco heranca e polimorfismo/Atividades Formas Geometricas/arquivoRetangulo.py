from arquivodasFormas import Formas

class Retangulo(Formas):
    def __init__(self, lado, altura):
        super().__init__(lado, altura)

    def calcularArea(self, lado, altura):
        area = lado * altura
        return area
    
primeiro_calculo = Retangulo(10,30)

print(primeiro_calculo.calcularArea(primeiro_calculo.lado,primeiro_calculo.altura))
