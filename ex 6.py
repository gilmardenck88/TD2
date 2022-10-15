#  Leia um vetor com 20 números inteiros. Escreva os elementos do vetor
# eliminando elementos repetidos.
numeros = list()
for c in range(0, 21):
    n = int(input('digite um valor: '))
    if n not in numeros:
        numeros.append(n)



print(f'voce digitou os valores  {numeros}, excluindo os repetidos ')

