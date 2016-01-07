# -*- coding: utf-8 -*-

"""
    Faça um Programa que peça a temperatura em graus Celsius, 
    transforme e mostre em graus Farenheit.
    
                celsius * (9/5) + 32
"""

temp = float(input("Digite a temperatura em Celsius: "))
print("{} ºC é Farenheit é {}".format(temp, temp * (9/5) + 32))