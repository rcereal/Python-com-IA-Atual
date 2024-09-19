from arquivoVeiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, tipo_guidon: str):
        super().__init__(marca, modelo, ano)
        self.tipo_guidon = tipo_guidon

    def informacoes(self):
        return f'{super().informacoes()}\nTipo de Guidon: {self.tipo_guidon}'
    
    def mover(self):
        return f'O motorista esta pilotando a {self.modelo}'