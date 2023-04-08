def menu_view(item: dict):
    global menu
    
    # print(item)
    
    if item['parent'] == 0: # Block for top-level item
        if list(menu.keys()).count(str(item['id'])) == 0: # If this item does not exists as top-level, must be added to the menu
            menu[str(item['id'])] = {
                'name': item['name'],
                'items': []
            }
        elif list(menu.keys()).count(str(item['id'])) > 0 and menu[str(item['id'])]['name'] == '': # If this item exist but does not have name, the name is updated
            menu[str(item['id'])]['name'] = item['name']
    else: # Block for "food-items"
        if list(menu.keys()).count(str(item['parent'])) != 0: #If this item belongs to a existent parent, is added to the list
            menu[str(item['parent'])]['items'].append(item)
        else: # If this item belongs to a parent that doesn't exists yet, then the parent is created
            menu[str(item['parent'])] = {
                'name': '',
                'items': [item,]
            }
    

if __name__ == '__main__':
    # CASE 1
    menu_list: list = [
        {
            'id': 1,
            'name' : 'Premium Sandwiches',
            'price' : 0,
            'vegetarian': False,
            'parent' : 0
        },
        {
            'id': 2,
            'name' : 'Seafood Soup',
            'price' : 12.00,
            'vegetarian': False,
            'parent' : 5
        },
        {
            'id': 3,
            'name' : 'Beacon Burger',
            'price' : 6.80,
            'vegetarian': False,
            'parent' : 1
        },
        {
            'id': 4,
            'name' : 'Cheese Burger',
            'price' : 5.60,
            'vegetarian': False,
            'parent' : 1
        },
        {
            'id': 5,
            'name' : 'Main Dishes',
            'price' : 0,
            'vegetarian': False,
            'parent' : 0
        },
        {
            'id': 6,
            'name' : 'Big Potato & Avocado Salad',
            'price' : 11.00,
            'vegetarian': True,
            'parent' : 5
        },
        {
            'id': 7,
            'name' : 'Coca Cola Zero',
            'price' : 2.50,
            'vegetarian': False,
            'parent' : 9
        },
        {
            'id': 8,
            'name' : 'Apple Juice',
            'price' : 3.50,
            'vegetarian': True,
            'parent' : 9
        },
        {
            'id': 9,
            'name' : 'Drinks',
            'price' : 0,
            'vegetarian': False,
            'parent' : 0
        },
        {
            'id': 10,
            'name' : 'Veggie Cheese Burger',
            'price' : 7.80,
            'vegetarian': True,
            'parent' : 1
        },
    ]
    
    # CASE 2
    # menu_list: list = [
    #     {
    #         'id': 1,
    #         'name' : 'Chinese Food',
    #         'price' : 0,
    #         'vegetarian': False,
    #         'parent' : 0
    #     },
    #     {
    #         'id': 2,
    #         'name' : 'Thai Food',
    #         'price' : 0,
    #         'vegetarian': False,
    #         'parent' : 0
    #     },
    #     {
    #         'id': 3,
    #         'name' : 'Chilean Food',
    #         'price' : 0,
    #         'vegetarian': False,
    #         'parent' : 0
    #     },
    #     {
    #         'id': 4,
    #         'name' : 'Paila Marina',
    #         'price' : 12.60,
    #         'vegetarian': False,
    #         'parent' : 3
    #     },
    #     {
    #         'id': 5,
    #         'name' : 'Carbonada',
    #         'price' : 8.80,
    #         'vegetarian': False,
    #         'parent' : 3
    #     },
    #     {
    #         'id': 6,
    #         'name' : 'Curanto en Hoyo',
    #         'price' : 18.00,
    #         'vegetarian': False,
    #         'parent' : 3
    #     },
    #     {
    #         'id': 7,
    #         'name' : 'Coconut Spicy Rice',
    #         'price' : 5.50,
    #         'vegetarian': False,
    #         'parent' : 2
    #     },
    #     {
    #         'id': 8,
    #         'name' : 'Milky Spicy Noodles',
    #         'price' : 5.50,
    #         'vegetarian': False,
    #         'parent' : 2
    #     },
    #     {
    #         'id': 9,
    #         'name' : 'Pork Chaufan Rice',
    #         'price' : 4.60,
    #         'vegetarian': False,
    #         'parent' : 1
    #     },
    #     {
    #         'id': 10,
    #         'name' : 'Vegetables Chapsui',
    #         'price' : 4.00,
    #         'vegetarian': True,
    #         'parent' : 1
    #     },
    # ]
    
    # CASE 3
    # menu_list: list = [
    #     {
    #         'id': 1,
    #         'name' : 'Green Detox',
    #         'price' : 3.30,
    #         'vegetarian': True,
    #         'parent' : 5
    #     },
    #     {
    #         'id': 2,
    #         'name' : 'Orange - Apple - Banana',
    #         'price' : 3.00,
    #         'vegetarian': True,
    #         'parent' : 5
    #     },
    #     {
    #         'id': 3,
    #         'name' : 'Citric Fresh',
    #         'price' : 3.00,
    #         'vegetarian': True,
    #         'parent' : 5
    #     },
    #     {
    #         'id': 4,
    #         'name' : 'Red Apple Punch',
    #         'price' : 3.30,
    #         'vegetarian': True,
    #         'parent' : 5
    #     },
    #     {
    #         'id': 5,
    #         'name' : 'Natural Bio Drinks',
    #         'price' : 0,
    #         'vegetarian': False,
    #         'parent' : 0
    #     },
    #     {
    #         'id': 6,
    #         'name' : 'Banana Milkshake',
    #         'price' : 3.80,
    #         'vegetarian': False,
    #         'parent' : 10
    #     },
    #     {
    #         'id': 7,
    #         'name' : 'Coconut - Custard Apple - Milk',
    #         'price' : 4.0,
    #         'vegetarian': False,
    #         'parent' : 10
    #     },
    #     {
    #         'id': 8,
    #         'name' : 'Strawberry Milkshake w/cream',
    #         'price' : 4.50,
    #         'vegetarian': False,
    #         'parent' : 10
    #     },
    #     {
    #         'id': 9,
    #         'name' : 'Hot Chocolate w/milk',
    #         'price' : 4.0,
    #         'vegetarian': False,
    #         'parent' : 10
    #     },
    #     {
    #         'id': 10,
    #         'name' : 'Sweet Drinks',
    #         'price' : 0,
    #         'vegetarian': False,
    #         'parent' : 0
    #     },
    # ]
    
    menu = {}
    
    # Input reception
    for item in menu_list:
        menu_view(item)
        
    #print(menu)
    
    # Output print
    print('### WELCOME TO OUR MENU ###\n')
    for parent in menu:
        print(f' - {menu[parent]["name"].upper()} - \n')
        # print(f'{menu[parent]["items"]} \n')
        
        # Second loop for items
        for i in menu[parent]["items"]:
            print(f'\t{i["name"]}')
            print(f'\tprice : {i["price"]} usd')
            if i['vegetarian'] == True: print('\tVegetarian Option!')
            print('\n')