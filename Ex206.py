﻿# ~*~ coding: utf-8 ~*~

'''
Задача "День рождения"

На день рождения пришли N человек. В некоторый момент именинник
решил, что пора устроить какую-нибудь игру. Он выяснил, что i-й человек
согласен вступить в игру, если в ней уже принимают участие не менее
A[i] и не более B[i] человек. Единожды вступив в игру, никто из нее
не выходит. Требуется выяснить, может ли именинник установить такую
последовательность вступления в игру, что в итоге все
присутствующие станут ее участниками. (Сам именинник в игре участия
не принимает.)

Входные данные.
Сначала вводится количество гостей N (1≤N≤100). Затем вводится
N пар чисел A[i] и B[i] (все эти числа из диапазона от 0 до N-1).

Выходные данные.
Если можно установить последовательность вступления гостей в игру,
чтобы в итоге все стали ее участниками, то нужно вывести номера гостей
в том порядке, в каком они могут вступать в игру. Если всех вовлечь
в игру не удастся, выведите одно число - 0.

Пример 1
Пример входного файла
5
4 4
0 3
1 4
1 3
2 2

Пример выходного файла
2 3 5 4 1

Пример 2
Пример входного файла
3
1 1
1 1
1 1

Пример выходного файла
0

Пример 3
Пример входного файла
1
0 0

Пример выходного файла
1
'''

def sort(A, B, C):
    i=0
    while i < len(A)-1:
        j = 0
        while j < len(A) - i - 1:
            if A[j] > A[j+1]:
                buf = A[j]
                A[j] = A[j+1]
                A[j+1] = buf
                buf = B[j]
                B[j] = B[j+1]
                B[j+1] = buf
                buf = C[j]
                C[j] = C[j+1]
                C[j+1] = buf
            j+=1
        i+=1

if __name__ == '__main__':
    n = int(input())
    A = []
    B = []
    C = []
    for i in range(n):
        r1, k1 = map(int, input().split())
        A.append(r1)
        B.append(k1)
        C.append(i+1)
    sort(A, B, C)
    res = []
    
    while len(res) < n:
        if A[0] <= len(res):
            j = 0
            ming = j
            while j < len(A) and A[j] <= len(res):
                if B[j] < B[ming]:
                    ming = j
                j+=1
            res.append(str(C[ming]))
            del(A[ming])
            del(B[ming])
            del(C[ming])
        else:
            print ('0')
            break
        
    print(' '.join(res))