from pprint import pprint

cook_book = {}


def get_cook_book_with_quantity():
    with open('recipes.txt', encoding='utf-8') as f:
        while True:
            name = f.readline().strip()
            if not name:
                break
            count = int(f.readline().strip())
            cook_book[name] = []
            line = f.readline().strip()
            while line:
                ingredients = line.split(" | ")
                ingredients_dict = {"ingredient_name": ingredients[0],
                                    "quantity": int(ingredients[1]),
                                    "measure": ingredients[2]}
                cook_book[name].append(ingredients_dict)
                line = f.readline().strip()
    return cook_book


# pprint(get_cook_book_with_quantity())


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


# pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
