class Veiculo:
    def __init__(self, marca:str, modelo:str, ano:int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def informacoes(self):
        return f'Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}'

    def mover(self):
        return 'O veiculo esta se movendo...'
    