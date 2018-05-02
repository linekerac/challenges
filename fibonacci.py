# -*- coding: utf-8 -*-

x = int(input("Digite um número: "))
a, b = 0, 1

for i in range(x):
    print('{}'.format(a), end=" ")
    a, b = b, a+b


