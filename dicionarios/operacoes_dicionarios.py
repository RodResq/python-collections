meu_dicionario = {1 : 'Fabio', 2 : 'Maria', 3 : 'Joao', 4 : 'Jose'}
meu_dicionario_2 = {'nome' : 'Joao', 'sobrenome' : 'Silva', 'idade' : 50}

#Get()
print(meu_dicionario.get(2))
print(meu_dicionario[2])

print(meu_dicionario_2.get('sobrenome'))

#Len()
print(len(meu_dicionario))

#Pop()
meu_dicionario.pop(1)
# del meu_dicionario[1]
print(meu_dicionario)

#Clear()

# meu_dicionario.clear()
# print(meu_dicionario)

#Keys()
# print(meu_dicionario.keys())
# print(meu_dicionario_2.keys())

#Adcionando elementos
meu_dicionario[5] = 'Joaquina'
# print(meu_dicionario)
meu_dicionario_2.update({'profissao' : 'Programador'})
