#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

num1 = int(input("Digite um número : "))
num2 = int(input("Digite outro número : "))

op = input("Digite uma operação: ")

if op == "+":
    print("A soma de %d e %d é : %d."%(num1, num2, num1 + num2))

elif op == "-":
    print("A subtração de %d e %d é %d."%(num1, num2, num1 - num2))

elif op == "*":
    print("A multiplicação de %d e %d é %d."%(num1, num2, num1 * num2))

elif op == "/":
    print("A divisão de %d por %d é %d."%(num1, num2, num1 / num2))

elif op == "**":
    print("O número %d elevado a %d é %d."%(num1, num2, num1 ** num2))

else:
    print("Opção Inválida!")



