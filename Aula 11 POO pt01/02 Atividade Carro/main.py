from arquivoCarro import Carro

modelo = input('Qual modelo do carro: ')
marca = input('Qual a marca do carro: ')
ano = int(input('Qual o ano do carro: '))
cor = input('Qual a cor do carro: ')
velocidade = int(input('Qual a velocidade do carro em Kmh: '))

primeiro_carro = Carro(modelo, marca, ano, cor, velocidade)

primeiro_carro.acelerar(15)
primeiro_carro.desacelerar(20)

print(primeiro_carro.__dict__)