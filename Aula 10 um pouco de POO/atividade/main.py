from cachorro import Cachorro

#objeto 1
primeiro_cachorro = Cachorro('Charles','Bull Terrier','55kg')

#objeto 2
segundo_cachorro =  Cachorro('Beto','Poodle','20kg')

print(primeiro_cachorro.__dict__)
print(segundo_cachorro.nome,segundo_cachorro.raca,segundo_cachorro.peso)