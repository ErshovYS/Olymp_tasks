﻿# ~*~ coding: utf-8 ~*~

'''
Задача. "Список"

В фирме, выпускающей компьютерные комплектующие, все изделия
получают последовательные номера от 1 до N. Каждое изделие после
его изготовления поступает в отдел контроля качества, где оно
проверяется, и либо уходит в продажу, либо заносится в список
бракованных изделий и списывается. К сожалению, список бракованных изделий
иногда оказывается чересчур длинным. Тогда для его сокращения подряд
идущие числа заменяются интервалом: через тире указываются номера
первого и последнего изделия интервала. Например, вместо
1,3,4,5,6,7,8,10,12,16,17,20,21,22,23,24
записывается
1,3-8,10,12,16-17,20-24

Напишите программу, которая по полному списку номеров бракованных
изделий, выдаст этот список в сокращенном виде.

Входные данные.
Вводится сначала число N - общее количество изделий.
Затем число M - количество изделий, оказавшихся бракованными.
Далее вводятся в возрастающем порядке номера бракованных изделий.

Выходные данные. Выведите в одной строке список номеров бракованных изделий
в сокращенном виде. Интервалы должны разделяться запятой.
В строке не должно быть пробелов.

Ограничения
Подзадача 1. 1≤M≤N≤100.
Подзадача 2. 1≤M≤N≤1000000.

Пример 1 (подзадача 1)
Пример ввода
10 5
1 3 5 7 9

Пример вывода
1,3,5,7,9

Пример 2 (подзадача 1)
Пример ввода
40 16
1 3 4 5 6 7 8 10 12 16 17 20 21 22 23 24

Пример вывода
1,3-8,10,12,16-17,20-24

Пример 3 (подзадача 1)
Пример ввода
11 11
1 2 3 4 5 6 7 8 9 10 11

Пример вывода
1-11

Пример 4 (подзадача 2)
Пример ввода
10000 1
5

Пример вывода
5
'''



if __name__ == '__main__':
    n, m = map(int, input().split())
    numss = list(map(int, input().split()))
    
    res = str(numss[0])
    ins = True
    for ind, i in enumerate(numss):
        if ind > 0:
            if i-1 == numss[ind-1]:
                if ins:
                    res = u'{0}-'.format(res)
                    ins = False
            else:
                if not ins:
                    res = u'{0}{1}'.format(res, str(numss[ind-1]))
                res = u'{0}, {1}'.format(res, str(i))
                ins = True
    if res[len(res)-1] == u'-':
        res = u'{0}{1}'.format(res, str(numss[-1]))  
    print(res)