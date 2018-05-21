# ~*~ coding: utf-8 ~*~

'''
Задача "Ход конем"

Шахматная ассоциация решила оснастить всех своих сотрудников такими
телефонными номерами, которые бы набирались на кнопочном телефоне
ходом коня. Например, ходом коня набирается телефон 340-4927. При
этом телефонный номер не может начинаться ни с цифры 0, ни с цифры 8.

Клавиатура телефона выглядит так:
789
456
123
 0


Напишите программу, определяющую количество телефонных номеров
длины N, набираемых ходом коня.

Входные данные
Во входном файле записано целое число N (1≤N≤100).

Выходные данные
Выведите в выходной файл искомое количество телефонных номеров.

Пример входного файла
2

Пример выходного файла
16
'''

def rec_list(main_list, num):
    new_list = []
    new_list.append(main_list[num-1][4] + main_list[num-1][6]) # 0
    new_list.append(main_list[num-1][6] + main_list[num-1][8]) # 1
    new_list.append(main_list[num-1][7] + main_list[num-1][9]) # 2
    new_list.append(main_list[num-1][4] + main_list[num-1][8]) # 3
    new_list.append(main_list[num-1][0] + main_list[num-1][3] + main_list[num-1][9]) # 4
    new_list.append(0) # 5
    new_list.append(main_list[num-1][0] + main_list[num-1][1] + main_list[num-1][7]) # 6
    new_list.append(main_list[num-1][2] + main_list[num-1][6]) # 7
    new_list.append(main_list[num-1][1] + main_list[num-1][3]) # 8
    new_list.append(main_list[num-1][2] + main_list[num-1][4]) # 9
    main_list.append(new_list)
    
if __name__ == '__main__':
    n = int(input())
    f_list = []
    for i in range(10):
        f_list.append(1)
    main_list = [f_list]
    a = 1
    while a < n:
        rec_list(main_list, a)
        a += 1
    res = 0
    for i in range(10):
        if i not in [0, 8]:
            res += main_list[-1][i]
    print(res)