# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

n = int(input('Введите общее количество сделанных журавликов: '))
# Исходя из условия Катя проделывает 2/3 всей работы, Петя и Сережа по 1/6

Petya = n * (1/6)
Serezha = n * (1/6)
Katya = n * (2/3)
print(f'Петя сделал: {Petya} журавликов, Катя сделала {Katya} журавликов, Серёжа сделал {Serezha} журавликов')