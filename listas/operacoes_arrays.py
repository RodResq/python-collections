from array import array

array_1 = array('B', [1, 2, 3, 4, 5, 6])

array_2 = array('u', ['O', 'L', 'A'])


for i in array_2:
    print(i)

# print(array_1)
#
# for i in array_1:
#     print(i)

# Inserir elementos no Array
array_1.insert(2, 50)
# for i in array_1:
#     print(i)

# Removendo Elementos do array
array_1.remove(4)
#
# for i in array_1:
#     print(i)

# Buscar elemento em um array
# print(array_1.index(50))

# Atualizar dados em um array
array_1[2] = 55

for i in array_1:
    print(i)
