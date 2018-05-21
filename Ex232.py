# ~*~ coding: utf-8 ~*~

'''
Задача "Гвоздики"
На прямой дощечке вбиты гвоздики. Любые два гвоздика можно соединить
ниточкой. Требуется соединить какие-то пары гвоздиков ниточками так,
чтобы к каждому гвоздику была привязана хотя бы одна ниточка, а
суммарная длина всех ниточек была минимальна.

Входные данные
В первой строке входного файла записано число N - количество
гвоздиков (2 ≤ N ≤ 100). В следующей строке записано N чисел -
координаты всех гвоздиков (неотрицательные целые числа,
не превосходящие 10000).

Выходные данные
В выходной файл нужно вывести единственное число -
минимальную суммарную длину всех ниточек.


Пример входного файла    
5
4 10 0 12 2

0 1 3 6 12 24 48

Пример выходного файла
6

33
'''

# Разбор из интернета
def focus(nums):
    res = [9999, nums[1]-nums[0]]
    i = 2
    while i < len(nums):
        res.append(min(res[i-1], res[i-2]) + nums[i]-nums[i-1])
        i += 1
    return res[i-1]

if __name__ == '__main__':
    #n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    bools = []
    for i in range(len(nums)):
        bools.append(0)
    res = nums[1] - nums[0]
    bools[0] = 1
    bools[1] = 1
    if len(nums) > 2:
        res += nums[len(nums)-1] - nums[len(nums)-2]
        bools[len(nums)-1] = 1
        bools[len(nums)-2] = 1
    i = 2
    while i < len(nums)-2:
        if bools[i] > 0:
            i+1
        else:
            if nums[i]-nums[i-1] > nums[i+1]-nums[i]:
                res += nums[i+1]-nums[i]
                bools[i] += 1
                bools[i+1] += 1
                print (nums[i], '-', nums[i+1])
                i += 2
            else:
                res += nums[i]-nums[i-1]
                bools[i] += 1
                bools[i-1] += 1
                print (nums[i-1], '-', nums[i])
                i += 1
    
    i = 2
    while i < len(nums)-2:
        if bools[i] == 2:
            if bools[i-1] == 2 and bools[i+1] == 2:
                if nums[i]-nums[i-1] > nums[i+1]-nums[i]:
                    res -= nums[i]-nums[i-1]
                    bools[i] -= 1
                    bools[i-1] -= 1
                    print (nums[i-1], '|', nums[i])
                else:
                    res -= nums[i+1]-nums[i]
                    bools[i] -= 1
                    bools[i+1] -= 1
                    print (nums[i], '|', nums[i+1])
            elif bools[i-1] == 2:
                res -= nums[i]-nums[i-1]
                bools[i] -= 1
                bools[i-1] -= 1
                print (nums[i-1], '|', nums[i])
        i += 1
    print('Мой ответ: ', res)
    print('Вариант из интернета: ', focus(nums))