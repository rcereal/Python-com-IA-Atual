from arquivodasFormas import Formas

class Triangulo(Formas):
    def __init__(self, lado, altura):
        super().__init__(lado, altura)

    def calcularArea(self, base, altura):
        area = base * altura / 2
        return area
    
calculoTriangulo = Triangulo(50, 100)

print(calculoTriangulo.calcularArea(calculoTriangulo.lado, calculoTriangulo.altura))