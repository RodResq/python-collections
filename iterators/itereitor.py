lista_simples_inteiros = [1, 2, 3, 8, 14, 4, 5]

meu_iter = iter(lista_simples_inteiros)

while True:
    try:
        elemento = next(meu_iter)
        print(elemento)
    except StopIteration:
        break

# print(next(meu_iter))
# print(next(meu_iter))
# print(next(meu_iter))
# print(next(meu_iter))
# print(next(meu_iter))
# print(next(meu_iter))
# print(next(meu_iter))
# print(next(meu_iter))
