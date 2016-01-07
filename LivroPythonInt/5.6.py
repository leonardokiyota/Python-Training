#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
    Tabuada
'''

n = int(input("Digite um número: "))

x = 1

while x <= 10:
    print("%d x %d = %d"%(n, x, n*x))
    x=x+1
