#!/usr/bin/env python3
# *- encoding: utf-8 -*-

'''
    Escreva um programa para a provar o empréstimo para comprar uma casa. O
    programa deve perguntar o valor da casa, o salário e a quantidade de anos
    a pagar. O valor da prestação não pode ser superior a 30% do salário.
    Calcule o valor da prestação sendo o valor da casa a comprar dividindo
    pelo número de meses.
'''

valcasa = float(input("Digite o valor da casa: "))
sal = float(input("Digite o seu salário: "))
parc = int(input("Digite a quantidade de parcelas: "))
total = valcasa / parc

if total > sal * 0.30:
    print("A parcela excede o 30%% do seu salário cada parcela sai R$%.2f."%total)

else:
    print("Pode comprar e cada parcela sai R$%.2f."%total)
