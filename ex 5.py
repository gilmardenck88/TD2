# Faça um programa que leia um vetor de 10 posições e verifique se
# existem valores iguais e os escreva na tela.
dados = []
valores = []
repetidos = set()

for c in range(0, 11):
    num = int(input('digite um valor: '))
    dados.append(num)
for dado in dados:
    if dado not in valores:
        valores.append(dado)
    else:
        repetidos.add(dado)
print(f'valores digitados = {dados}')
print(f' valores repetidos = {repetidos}')








