# Дан вот такой (уже многомерный!) список:
#
# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
#
# Напишите код, который «раскрывает» все вложенные списки, то есть оставляет только внешний список.
# Для решения используйте только list comprehensions.
#
# Ответ: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

# for x in range(len(nice_list)):
#     for _ in range(len(nice_list[x])):
#         for i in range(len(nice_list[x][_])):
#             new_list.append(nice_list[x][_][i])
new_list = [nice_list[x][_][i] for x in range(len(nice_list)) for _ in range(len(nice_list[x])) for i in range(len(nice_list[x][_]))
]
print(new_list)