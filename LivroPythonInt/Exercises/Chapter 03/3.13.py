#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
   Escreva um programa que converta Celsius em Farenheit.
'''

celsius = float(input("Digite a temperatura em Graus Celsius: "))
fare = ((9 * celsius) / 5 )+ 32

print("A temperatura em C=%.2f em Celsius convertido em Farenheit é F=%.2f."%(celsius, fare))
