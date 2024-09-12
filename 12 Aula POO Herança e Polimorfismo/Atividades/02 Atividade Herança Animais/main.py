from arquivoAnimal import  Animal
from arquivoCachorro import Cachorro
from arquivoGato import Gato


primeiro_cachorro = Cachorro('Fred',  3, 'Pitbull')
print(primeiro_cachorro.__dict__)
print(primeiro_cachorro.som())

primeiro_gato = Gato('Nami', 2, 'Preto')
print(primeiro_gato.__dict__)
print(primeiro_gato.som())