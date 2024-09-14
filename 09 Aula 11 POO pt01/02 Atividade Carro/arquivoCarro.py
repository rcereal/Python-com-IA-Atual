class Carro:
    def __init__(self, modelo:str, marca:str, cor:str, ano:int, velocidade:int = 0):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.velocidade = velocidade

    def acelerar(self,aumentar_velocidade):
        self.velocidade += aumentar_velocidade
        return self.velocidade
    
    def desacelerar(self, diminuir_velocidade):
        self.velocidade -= diminuir_velocidade
        return self.velocidade
