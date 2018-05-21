# ~*~ coding: utf-8 ~*~

'''
Задача "Шаблон и слово"
Требуется определить подходит ли заданное слово под заданный шаблон.
Шаблон задается большими латинскими буквами, знаками "?" -
любой символ, "*" - любая последовательность символов (даже пустая).

Входные данные: в первых двух строках записаны шаблон и слово:
в одной строки записан шаблон - последовательность больших
латинских букв, "?" и "*", в другой  - слово, состоящее только
из больших латинских букв (строки короче 100 символов).

Выходные данные: вывести YES, если слово подходит или NO, если нет.

Примеры
input.txt
ABBCDA
A*CDA

output.txt
YES

input.txt
AADAAVA
A*DA*AA*

output.txt
NO
'''
    
if __name__ == '__main__':
    s = input()
    temp = input()
    i = 0
    j = 0
    equa = True
    while i < len(temp):
        if temp[i] not in ['?', '*']:
            if temp[i] != s[j]:
                equa = False
                break
            i+=1
            j+=1
        elif temp[i] == '?':
            i+=1
            j+=1
        elif temp[i] == '*':
            if i == len(temp)-1:
                i+=1
            elif temp[i+1] != '?':
                if s[j] == temp[i+1]:
                    i+=1
                else:
                    while j < len(s):
                        if (s[j] == temp[i+1]):
                            i+=1
                            break
                        else:
                            j+=1
                    else:
                        equa = False
                        break
            else:
                while temp[i] in ['?', '*']:
                    if temp[i] == '?':
                        j+=1
                    i+=1
                while j < len(s):
                    if s[j] != temp[i]:
                        j+=1
                    else:
                        break
                else:
                    equa = False
                    break
                    
    if equa:
        print('YES')
    else:
        print('NO')