#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
    Tabuada
'''

n = int(input("Digite um número: "))
fim = int(input("Digite o final do número que você deseja multiplicar: "))

x = 0

while x <= fim:
    print("%d x %d  =  %d"%(n, x, n*x))
    x+=1

