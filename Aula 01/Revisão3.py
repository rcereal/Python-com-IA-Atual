import os
os.system ('cls')


numeros = []  # Lista vazia para armazenar os números

contador = 0  # Inicializa o contador

while contador < 10:  # Enquanto o contador for menor que 10
    numero = int(input("Digite um número: "))  # Solicita um número do usuário e converte para inteiro
    numeros.append(numero)  # Adiciona o número à lista
    contador += 1  # Incrementa o contador

print(f'Números digitados: {numeros}')

quantidade_de_pares = 0
quantidade_de_impares = 0

for num in numeros:
    if num % 2 == 0:
        quantidade_de_pares += 1
    else:
        quantidade_de_impares =+1

print(f'Quantidade de números pares: {quantidade_de_pares}')
print(f'Quantidade de números ímpares: {quantidade_de_impares}')