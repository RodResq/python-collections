import copy

nested_list = [[1, 2, True], ["Ola", "Mundo"]]

# Deep Copy
nova_lista = copy.deepcopy(nested_list)
nested_list[0][1] = "A"
print(nova_lista)
print(nested_list)

# Shallow Copy - copia referencia - end de memoria
outra_lista = copy.copy(nested_list)
nested_list[0][1] = "B"
print(outra_lista)
print(nested_list)

