# 3. Faça um programa que preenche um vetor com valores inteiros até que
# o usuário digite um valor negativo (o valor negativo não deve ser
# inserido no vetor). Imprima:
# a. O vetor.
# b.  A quantidade de valores maiores que 5.
# c. A soma dos valores pares armazenados no vetor.
# d.  A soma dos valores ímpares armazenados no vetor.
# e. A quantidade total de valores armazenados no vetor.


vetor = []
par = 0
impar = 0
cont = 0
while True:
    num = (int(input('digite um valor: ')))
    if num >= 0:
        vetor.append(num)
    if num > 5:
        cont += 1
    if num % 2 == 0 and num > 0:
        par += num
    if num % 2 != 0 and num > 0:
        impar += num

    if num <= 0:
        break

print(vetor)
print(f'a quantidade total de valores digitados é: {len(vetor)}')
print(f'foram digitados {cont} numeros maior que 5.')
print(f'a soma dos numeros pares digitados é: {par}')
print(f'a soma dos numeros impares digitados é: {impar}')

