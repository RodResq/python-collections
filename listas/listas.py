lista_simples_inteiros = [1, 2, 3, 8, 14, 4, 5]
lista_simples_string = ["Ola", "Mundo"]
lista_simples_mescladas = [1, 2, 3, "Ola Mundo", True, 1.5]
nested_list = [[1, 2, True], ["Ola", "Mundo"]]

print(lista_simples_inteiros)
print(nested_list)

#Len()
print(len(lista_simples_mescladas))
print(len(nested_list))

#Append()
lista_simples_inteiros.append(6)
print(lista_simples_inteiros)

#Insert()
# lista_simples_inteiros.insert(2, "Ola")
# print(lista_simples_inteiros)

#Remove()
lista_simples_inteiros.remove(1)
print(lista_simples_inteiros)

#Index()
index = lista_simples_inteiros.index(3)
print(index)

#Count()
count = lista_simples_inteiros.count(3)
print(count)

#Sort() - Muda a ordem da lista permantemente
lista_string = ["A", "B", "C"]
lista_string.sort(reverse=True)
print(lista_string)

#Sorted() - Muda a ordem da lista temporariariamente
lista_carros = ["bmw", "audi", "toyota", "subaru"]
print("Here is the original list:")
print(lista_carros)

print("\nHere is the sorted list:")
print(sorted(lista_carros))

print("\nHere is the original list again:")
print(lista_carros)

#Reverse() - Inverte a ordem da lista de forma permanente
print("\ninvertendo a lista")
lista_carros.reverse()
print(lista_carros)
