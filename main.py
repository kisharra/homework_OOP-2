def create_cook_book(file):  #функция для создания словаря
    cook_book = {}
    current_recipe = ''
    for line in file.split('\n'):
        line = line.strip()
        if line:
            if current_recipe == '':
                current_recipe = line
                cook_book[current_recipe] = []
            else:
                if line.isdigit():
                    continue
                else:
                    ingredient_name, quantity, measure = line.split(' | ')
                    cook_book[current_recipe].append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
        else:
            current_recipe = ''
    return cook_book

with open('recipes.txt') as file:  #чтение файла с вызовом функции создания словаря
    cook_book = create_cook_book(file.read())

def get_shop_list_by_dishes(dishes, person_count):  #функция для поиска ингредиентов
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] not in shop_list:
                    shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
                else:
                    shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    return shop_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)) #вывод результата
