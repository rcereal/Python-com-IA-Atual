from arquivoautomoveis import Automovel
from arquivocarros import Carro

primeiro_automovel = Automovel('Honda',10)
print(primeiro_automovel.acelerar(50))

primeiro_carro = Carro('AudiTT', 100, 'Audi', 'Audi', 2023)
print(primeiro_carro.__dict__)  