myBagres = ['Navarro', 'Atuesta', 'Lopez']
print('Entre o nome de um bagre')
name = input()
if name not in myBagres:
    print('Nao existe um bagre chamado ' + name)
else:
    print(name + ', esse é bagre.')