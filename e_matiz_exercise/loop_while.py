toppings = ['cheese', 'masarella', 'meat']
pizza = {'masarella_pizza': toppings}
switch_for_pizza = True
prompt = '\n для завершення заказа напишіть end'
prompt += '\n введіть добавку до піци: '
while switch_for_pizza:
    top_adding = input(prompt)
    if top_adding != 'end':
        print(top_adding)
        toppings.append(top_adding)

    else:
        switch_for_pizza = False
        for key_p, value_p in pizza.items():
            print(key_p + ':')
            for value in value_p:
                print(f'{value}')
