class Automovel:
    def __init__(self, nome:str, velocidade:int):
        self.nome = nome
        self.velocidade = velocidade

    def acelerar(self,aumentar_velocidade):
        self.velocidade += aumentar_velocidade
        return self.velocidade
    def desacelerar(self,diminuir_velocidade):
        self.velocidade -= diminuir_velocidade
        return self.velocidade
