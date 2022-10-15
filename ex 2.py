# 2. Faça um programa que preenche  um vetor de  50 posições com valores
# aleatórios entre 0 e 20 e encontre:
# Obs: Para fazer um vetor de tamanho 50 preenchido com 0 é possível fazer:
# vetor = [0] * 50. Note que o valor 50 também pode ser substituído por uma variável
# qualquer.
# a. A soma dos valores armazenados no vetor.
# b.  O número de ocorrências do valor 9.
# c. O maior valor armazenado no vetor.
# d.  O menor valor armazenado no vetor.




from random import randint

num = (randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20),
       randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20),
       randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20),
       randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20),
       randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20),
       randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20),
       randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20),
       randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20),
       randint(0, 20), randint(0, 20))
for n in num:
    print(f'{n}')
print(f'a soma de todos so numeros do vetor é: {sum(num)}')
print(f'o valor 9 apareceu {num.count(9)} vezes')
print(f'o maior valor armazenado foi {max(num)}')
print(f'o maior valor armazenado foi {min(num)}')

