# palestrantes = (['Ana, Procedimentos Esteticos, Stetic'], ['Carlos, Python com IA, Infinity'], ['Jose, Logica de Programação, BYD'])

# print(palestrantes[2])

# DESAFIO

Equipe_cão = (10,3,5)
Equipe_bola = (8,2,6)
Equipe_Hum = (5,3,4)

equipes = (Equipe_cão, Equipe_bola, Equipe_Hum)

medias = []

for equipe in equipes:
    medias.append(sum(equipe[1])/len(equipe[1]))

print(medias)

