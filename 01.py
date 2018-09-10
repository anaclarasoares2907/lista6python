'''
Ana Clara
Questão 01
'''
lista = list()
for n in range(5):
    l = int(input('Digite um número: '))
    lista.append(l)

maior = max(lista)
menor = min(lista)
pos_max = lista.index(maior)
pos_min = lista.index(menor)


print('Maior número é: ',maior)
print('Menor número é: ',menor)
print('Posição do maior número é: ',pos_max)
print('Posição do menor número digitado foi: ',pos_min)
