from collections import OrderedDict

import config


def food_to_dict(food: str) -> dict:
    food_dict = {}
    for product in [product.lower() for product in food.split()]:
        if product[-1].isdigit() and '_' in product:
            product, _, amount = product.rpartition('_')
            amount = float(amount)
            if product in food_dict:
                food_dict[product] += amount
            else:
                food_dict[product] = amount
        else:
            if product in food_dict:
                food_dict[product] += 1
            else:
                food_dict[product] = 1

    return food_dict


def not_found_products(food: dict) -> list:
    all_products = {'кофе', 'тыквенные_семечки', 'чечевица', 'мандарин', 'горох', 'морская_капуста', 'гранат', 'арахис',
                    'крабовое_мясо', 'лук_зеленый', 'слива', 'гречка', 'кинза', 'сосиска', 'молоко', 'салат_листовой',
                    'клубника', 'сметана', 'майонез', 'хлеб_белый', 'грецкий_орех', 'шпинат', 'болгарский_перец',
                    'капуста', 'хлеб_кукурузный', 'кабачок', 'кефир', 'яйцо', 'апельсин', 'булгур', 'йогурт', 'абрикос',
                    'банан', 'квашеная_капуста', 'арахисовая_паста', 'креветки', 'говядина', 'курица', 'морковь',
                    'черный_чай', 'виноград', 'нут', 'сливочное_масло', 'лук_порей', 'стручковая_фасоль',
                    'хурма', 'фасоль', 'хлеб_цельнозерновой', 'кунжут', 'брокколи', 'маш', 'желатин', 'цукини',
                    'сельдь', 'рис', 'хлеб_украинский', 'изюм', 'форель', 'помидор', 'свинина', 'соль',
                    'оливковое_масло', 'маслины', 'семечки', 'тофу', 'пельмени', 'редис', 'зеленый_горошек', 'груша',
                    'яблоко', 'имбирь', 'томатный_сок', 'фисташки', 'кета', 'индейка', 'свекла', 'лук', 'петрушка',
                    'зеленый_чай', 'киви', 'шампиньоны', 'бекон', 'овсянка', 'айсберг', 'соевый_соус', 'кукуруза',
                    'миндаль', 'жимолость', 'ежевика', 'бурый_рис', 'огурец', 'томатная_паста', 'кимчи', 'макароны',
                    'малина', 'авокадо', 'сыр', 'картофель', 'тунец', 'нори', 'творог', 'горький_шоколад', 'киноа',
                    'мед', 'колбаса', 'какао', 'рисовая_мука', 'фета', 'чеснок', 'торт', 'сливки', 'подсолнечное_масло',
                    'кокосовая_стружка', 'укроп', 'сгущенка', 'маринованный_огурец', 'слоеное_тесто', 'печенье',
                    'крыжовник', 'фунчоза', 'черная_смородина', 'курага', 'черника', 'чипсы', 'сидр', 'пиво',
                    'кокосовое_молоко', 'сыр_плавленый', 'рисовая_лапша', 'угорь', 'кальмар', 'манка',
                    'горчица', 'ананас', 'лимон', 'вишня', 'ветчина', 'брынза', 'пшеничная_мука',
                    'маскарпоне', 'соба', 'молочный_шоколад', 'фундук', 'соевое_молоко', 'соя', }

    not_found = [product for product in food.keys() if product not in all_products]

    return not_found


def suppl_to_dict(suppl: list) -> dict:
    cad3 = {'C': 54, 'E': 4.2, 'B5': 4.2, 'D': 6.9, 'A': 600,
            'B9': 360, 'B1': 0.9, 'B2': 0.9, 'B6': 0.9, 'Кальций': 540,
            'B12': 1.8, 'PP': 10.5}

    komplivit = {'B5': 5, 'C': 50, 'Железо': 5, 'E': 10, 'N': 2,
                 'B6': 5, 'Магний': 16.4, 'Кальций': 50.5, 'Медь': 0.75, 'B2': 1.27,
                 'Цинк': 2, 'B1': 1, 'PP': 7.5, 'B9': 100, 'Марганец': 2.5, 'A': 1135,
                 'B12': 12.5, 'P': 25}

    lutein_forte = {'Цинк': 7.5, 'Селен': 25, 'Медь': 1.5, 'P': 20, 'C': 50,
                    'E': 15, 'Лютеин': 4500, 'A': 500}

    haas = {'C': 60, 'B5': 6, 'B1': 1.4, 'B2': 1.6, 'B6': 2, 'B12': 1, 'PP': 18}

    askorbinka = {'C': 100}

    b12 = {'B12': 9}

    fish_fat = {'Омега3': 1000}

    suppl_dict = {}

    for s in suppl:
        if s == 'CaD3':
            for k, v in cad3.items():
                if k in suppl_dict:
                    suppl_dict[k] += v
                else:
                    suppl_dict[k] = v
        elif s == 'komplivit':
            for k, v in komplivit.items():
                if k in suppl_dict:
                    suppl_dict[k] += v
                else:
                    suppl_dict[k] = v
        elif s == 'lutein_forte':
            for k, v in lutein_forte.items():
                if k in suppl_dict:
                    suppl_dict[k] += v
                else:
                    suppl_dict[k] = v
        elif s == 'askorbinka':
            for k, v in askorbinka.items():
                if k in suppl_dict:
                    suppl_dict[k] += v
                else:
                    suppl_dict[k] = v
        elif s == 'B12':
            for k, v in b12.items():
                if k in suppl_dict:
                    suppl_dict[k] += v
                else:
                    suppl_dict[k] = v
        elif s == 'fish_fat':
            for k, v in fish_fat.items():
                if k in suppl_dict:
                    suppl_dict[k] += v
                else:
                    suppl_dict[k] = v
        elif s == 'haas':
            for k, v in haas.items():
                if k in suppl_dict:
                    suppl_dict[k] += v
                else:
                    suppl_dict[k] = v
    return suppl_dict


def nutrient_amount(food: dict, nutrients) -> dict:
    nutrient_dict = {'Селен': 0, 'B9': 0, 'C': 0, 'Лютеин': 0, 'Цинк': 0, 'Кальций': 0, 'Медь': 0, 'B1': 0, 'Фосфор': 0,
                     'Железо': 0, 'B12': 0, 'Кобальт': 0, 'Фтор': 0, 'Кремний': 0, 'Йод': 0, 'H': 0, 'D': 0, 'Хром': 0,
                     'PP': 0, 'E': 0, 'A': 0, 'B11': 0, 'B5': 0, 'Натрий': 0, 'K': 0, 'Калий': 0, 'Магний': 0, 'N': 0,
                     'P': 0, 'Марганец': 0, 'B6': 0, 'Молибден': 0, 'B2': 0, 'Омега3': 0,
                     'Белки': 0, 'Жиры': 0, 'Углеводы': 0, }

    for s in nutrient_dict.keys():
        nutrient_dict[s] = round(
            sum([nutrients[s][product] * food[product] for product in food if product in nutrients[s]]))

    return nutrient_dict


def resource_of_nutrients(my_nutrients, nutrients=config.nutrients, num_of_recommends=15) -> dict:
    resource = OrderedDict()

    for i in my_nutrients:
        resource[i] = list(OrderedDict(sorted(nutrients[i].items(), key=lambda t: t[1], reverse=True)).keys())[
                      :num_of_recommends]

    return resource


def nutrition(food: str, suppl: list):
    try:
        food_dict = food_to_dict(food)
    except (Exception,):
        return 'Ошибка в написании продуктов'
    else:
        suppl_dict = suppl_to_dict(suppl)
        not_found = not_found_products(food_dict)

        nutrient_dict = nutrient_amount(food_dict, config.nutrients)
        for k, v in suppl_dict.items():
            nutrient_dict[k] += v

        calorii = round(4.2 * nutrient_dict['Белки'] + 4.2 * nutrient_dict['Углеводы'] + 9.3 * nutrient_dict['Жиры'])

        return not_found, nutrient_dict, calorii
