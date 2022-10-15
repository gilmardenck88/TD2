# Faça um programa que leia um vetor de 15 posições e o compacte, ou
# seja, elimine as posições com valor zero. Para isso, todos os elementos
# a frente do valor zero, devem ser movidos uma posição para trás no
# vetor

numeros = []


for c in range(0, 15):
    n = int(input('digite um valor: '))
    if n != 0:
        numeros.append(n)
print(f'a lista de valores digitados compactada é: {numeros}')
