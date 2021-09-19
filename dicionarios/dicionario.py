meu_dicionario = {1 : 'Fabio', 2 : 'Maria', 3 : 'Joao', 4 : 'Jose'}
print(type(meu_dicionario))
meu_dicionario_2 = dict({1 : 'Fabio', 2 : 'Maria', 3 : 'Joao', 4 : 'Jose'})
print(type(meu_dicionario_2))

print(meu_dicionario[4])

for chave, valor in meu_dicionario.items():
    print(f"A chave e {chave} e o valor {valor}")

