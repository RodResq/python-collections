# Criando um set comprehensions
set_1 = {1, 2}
set_2 = {3, 4}

set_comprehensions = {i * i for i in range(0, 10)}
print(type(set_comprehensions))

set_comprehensions_2 = {i for i in set_1.union(set_2)}
print(type(set_comprehensions_2))
