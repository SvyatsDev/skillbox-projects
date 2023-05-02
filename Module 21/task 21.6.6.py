# Вы сделали для заказчика структуру сайта по продаже телефонов:
#
site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}
#
# Заказчик рассказал своим коллегам на рынке, и они тоже захотели такой сайт,
# только для своих товаров. Вы посчитали, что это лёгкая задача, и быстро принялись за работу.
#
# Напишите программу, которая запрашивает у клиента, сколько будет сайтов, а затем
# запрашивает название продукта и после каждого запроса выводит на экран активные сайты.
# Условия: структуру сайта нужно описать один раз, копипасту никто не любит.
# Подсказка: используйте рекурсию.

def site_structure(site, new_name, depth= 1, key= 'title'):
    if key in site:
        site[key] = f'Куплю/продам {new_name} недорого'
    for i_key, i_name in site.items():
        print(' ' * depth, i_key)
        if isinstance(i_name, dict):
            site_structure(i_name, new_name, depth + 1)
        else:
            print(' ' * (depth + 1), i_name)



n = int(input('Сколько будет сайтов? '))
for _ in range(n):
    name_site = input('Введите название сайта: ')
    site_structure(site, name_site)


