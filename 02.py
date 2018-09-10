'''
Ana Clara Soares
Questão 02
'''
lista = list()
while True:
    a = int(input('Digite um número: '))
    if a in lista:
        print('Digite um número diferente')
        continue
    else:
            lista.append(a)
    resp = input('Deseja continuar? s para sim n para não')
    print(lista)
    if resp == 'n':
        break
print(sorted(lista))
