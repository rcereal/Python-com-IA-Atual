# Crie uma hierarquia de classes representando formas geométricas. 
# Comece com uma classe base chamada "Forma" e, em seguida, crie classes 
# derivadas como "Círculo"e"Retângulo"que herdem da classe base.
# Adicione métodos para calcular área e perímetro emcada classe derivada.

class Formas:
    def __init__ (self, lado, altura):
        self.lado = lado
        self.altura = altura

    def calcularArea(self, area, altura):
        ...

    def calcularPerimetro(self, perimetro):
        ...