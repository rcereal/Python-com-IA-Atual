class Dono:
    def __init__(self, nome):
        self.nome = nome

class Carro:
    def __init__(self, modelo, marca, dono):
        self.modelo = modelo
        self.marca = marca
        self.dono = dono

objeto_dono = Dono('Guilherme')

objeto_carro = Carro('celta', 'chevrolet',objeto_dono.nome)

print(objeto_dono.__dict__)