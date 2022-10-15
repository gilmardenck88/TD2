# . Crie um programa com dois vetores de 10 posições e insira em outro
# vetor, nas posições pares, os valores do primeiro e, nas posições
# ímpares, os valores do segundo

num = [[], []]


for c in range(1, 11):
    n = int(input('digite um valor: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
print(f'os valores pares digitados são: {num[0]}')
print(f'os valores impares digitados são: {num[1]}')