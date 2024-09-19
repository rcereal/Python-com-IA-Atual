from arquivoVeiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, numero_portas: int):
        super().__init__(marca, modelo, ano)
        self.numero_portas = numero_portas

    def informacoes(self):
        return f'{super().informacoes()}\nNumero de Portas: {self.numero_portas}'
        
    def mover(self):
        return f'O motorista esta dirigindo o {self.modelo}'
    