minha_tupla = (1, 2, 3, "Ola Mundo", 1.5)
minha_tupla2 = 1, 2, 3, "Ola Mundo", 1.5, True

print(type(minha_tupla))
print(type(minha_tupla2))

#Count
print(minha_tupla.count(1))

#Index()
print(minha_tupla.index(3))

# Verificr a existencia de um elemento na tupla
print(2 in minha_tupla)

print(minha_tupla.__add__(minha_tupla2))
