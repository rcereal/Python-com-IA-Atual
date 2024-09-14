from arquivoautomoveis import Automovel

#A classe carro esta herdando os atributos e os metodos da classe automovel
class Carro(Automovel):
    def __init__(self, nome:str, velocidade:int, marca:str, modelo:str, ano:int):
        self.nome = nome
        self.velocidade = velocidade
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def acelerar(self,aumentar_velocidade):
        self.velocidade += aumentar_velocidade
        return f'O veiculos está a {self.velocidade} kmh.'
    def desacelerar(self,diminuir_velocidade):
        self.velocidade -= diminuir_velocidade
        return f'O veiculos está a {self.velocidade} kmh.'