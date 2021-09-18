lista_simples_inteiros = [1, 2, 3, 8, 14, 4, 5]

print(lista_simples_inteiros[0:4])
print(lista_simples_inteiros[1:])
print(lista_simples_inteiros[:3])
nova_lista = lista_simples_inteiros[:3]
print(nova_lista)

# Slice()
intervalo = slice(1, 4)
print(lista_simples_inteiros[intervalo])
