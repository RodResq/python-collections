pizza = {
    'crust': 'thick',
    'toppings': ['mussarela', 'extra cheese']
}

# Resumo do pedido
print(f"Your ordered a {pizza['crust']}-crust-pissa \n Whith the followings toppings:")

for toppings in pizza.get('toppings'):
    print(f"\t {toppings}")
