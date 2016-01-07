# -*- coding: utf:8 -*-

"""
     Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a 
     temperatura em graus Celsius.

                            C = (5 * (F-32) / 9). 
"""

temp = float(input("Digite a temperatura em Farenheit: "))

print("{} Farenheit em Celsius é {:.4f}ºC.".format(temp, 5 * (temp-32) / 9))

