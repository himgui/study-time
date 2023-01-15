catNames = []
while True:
    print('Digite o nome do gato' + str(len(catNames) + 1) +
    ' (Não digite nada para parar.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
    print('O nome dos gatos são: ')
    for name in catNames:
        print(' '+ name)