# ~*~ coding: utf-8 ~*~

'''
В прямоугольной таблице NxM (в каждой клетке которой записано
некоторое число) в начале игрок находится в левой верхней клетке.
За один ход ему разрешается перемещаться в соседнюю клетку
либо вправо, либо вниз (влево и вверх перемещаться запрещено).
При проходе через клетку с игрока берут столько у.е., какое число
записано в этой клетке (деньги берут также за первую
и последнюю клетки его пути).

Требуется найти минимальную сумму у.е., заплатив которую игрок может
попасть в правый нижний угол.

Входные данные
Во входном файле задано два числа N и M - размеры таблицы (1≤N≤20,
1≤M≤20). Затем идет N строк по M чисел в каждой - размеры штрафов
в у.е. за прохождение через соответствующие клетки (числа от 0 до 100).

Выходные данные
В выходной файл запишите минимальную сумму, потратив которую можно попасть
в правый нижний угол.

Пример входного файла
3 4
1 1 1 1
5 2 2 100
9 4 2 1

Пример выходного файла
8
'''

if __name__ == '__main__':
    m, n = map(int, input().split())
    matr = []
    for i in range(m):
        matr.append(list(map(int, input().split())))
        
    for i in range(m):
        for j in range(n):
            if i > 0 and j > 0:
                matr[i][j] += min(matr[i-1][j], matr[i][j-1])
            elif i > 0:
                matr[i][j] += matr[i-1][j]
            elif j > 0:
                matr[i][j] += matr[i][j-1]  
        
    print(matr[i][j])