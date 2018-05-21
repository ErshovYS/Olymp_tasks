# ~*~ coding: utf-8 ~*~

'''
Задача 3. "Подпоследовательности"

Дана последовательность, требуется найти длину наибольшей возрастающей
подпоследовательности.

Входные данные
В первой строке входного файла записано число N - длина последовательности
(1 ≤ N ≤ 1000). Во второй строке записана сама последовательность
(через пробел). Числа последовательности - целые числа,
не превосходящие 10000 по модулю.

Выходные данные
В выходной файл требуется вывести наибольшую длину возрастающей
подпоследовательности.

Пример входного файла
6
3 29 5 5 28 6

1  4  2  5  6  3  7

Пример выходного файла
3

5
'''

if __name__ == '__main__':
    #n = int(input())
    nums = list(map(int, input().split()))
    undernums = [[nums[0]]]
    maxres = 1
    for i in range(1, len(nums)):
        maxunder = undernums[0]
        for j in undernums:
            if len(j) > len(maxunder) and j[len(j)-1] < nums[i]:
                maxunder = j
        undernums.append(maxunder + [nums[i]])
        if len(maxunder)+1 > maxres:
            maxres = len(maxunder)+1
    print(undernums)
    print(maxres)