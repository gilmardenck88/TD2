# Crie um programa que lê 6 valores inteiros, armazene-os em um vetor e,
# em seguida, mostre na tela os valores lidos na ordem inversa.

vetor =[]

for c in range(0, 6):
    num = int(input('digite um valor: '))
    vetor.append(num)
vetor.sort(reverse=True)
print(vetor)