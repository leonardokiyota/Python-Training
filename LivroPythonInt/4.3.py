#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
    Escreva um programa que leia três números e que imprima o menor e o maior.
'''

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite outro número: "))

if num1 > num2 and num2 > num3:
    print("O maior é %d e o menor é %d - 1 ."%(num1, num3))
if num1 > num3 and num2 < num3:
    print("O maior é %d e o menor é %d - 4 ."%(num1, num2))


if num2 > num1 and num1 > num3:
    print("O maior é %d e o menor é %d - 2 ."%(num2, num3))
if num2 > num3 and num1 < num3:
    print("O maior é %d e o menor é %d - 5 ."%(num2, num1))


if num3 > num2 and num2 > num1:
    print("O maior é %d e o menor é %d - 3 ."%(num3, num1))
if num3 > num1 and num2 < num1:   
    print("O maior é %d e o menor é %d - 6 ."%(num3, num2))
