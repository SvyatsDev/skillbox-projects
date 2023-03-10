# N друзей постоянно берут в долг друг у друга деньги. В какой-то момент им надоело забывать,
# кто кому и сколько должен, и они придумали систему долговых расписок. И чтобы начать новый год «с чистого листа»,
# друзья решили оплатить все долговые расписки, которые накопились у них друг к другу. Однако выяснилось,
# что иногда один и тот же человек в разные дни выступал как в роли должника, так и в роли кредитора.
#
# Напишите программу, которая по заданным распискам вычислит, сколько всего должен каждый друг выплатить другим (или получить с других).
# Сначала вводится число N — количество друзей, затем вводится число K — количество долговых расписок,
# после этого следует K троек чисел: номер друга, взявшего в долг, номер друга, давшего деньги, и сумма.
# Гарантируется, что ни один друг не брал в долг сам у себя.
#
# Программа должна вывести «баланс друзей», то есть суммы, которые должны получить или отдать друзья.
# Положительное число означает, что друг должен получить деньги от других, отрицательное — должен отдать деньги.
#
# Пример 1:
# Кол-во друзей: 2
# Долговых расписок: 3
#
# 1 расписка
# Кому: 1
# От кого: 2
# Сколько: 10
#
# 1 расписка
# Кому: 1
# От кого: 2
# Сколько: 20
#
# 1 расписка
# Кому: 1
# От кого: 2
# Сколько: 20
#
# Баланс друзей:
# 1 : 50
# 2 : -50
#
# Пример 2:
# Кол-во друзей: 3
# Долговых расписок: 1
#
# 1 расписка
# Кому: 3
# От кого: 1
# Сколько: 100
#
# Баланс друзей:
# 1 : 100
# 2 : 0
# 3 : -100

n = int(input('Введите количество друзей: '))
k = int(input('Введите количество расписок: '))
cash = []
for i in range(n):
    cash.append([i+1, 0])
for _ in range(k):
    name_to = int(input('Кому? '))
    name_from = int(input('От кого? '))
    summ = int(input('Сколько? '))
    cash[name_to - 1][1] += summ
    cash[name_from - 1][1] -= summ
    print()
print('\nБаланс друзей: ')
for z in range(n):
    print(cash[z][0], ':', cash[z][1])