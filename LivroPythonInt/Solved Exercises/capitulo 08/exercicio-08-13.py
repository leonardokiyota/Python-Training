##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2014
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Primeira reimpressão - Outubro/2011
# Segunda reimpressão - Novembro/1012
# Terceira reimpressão - Agosto/2013
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Site: http://python.nilo.pro.br/
# 
# Arquivo: exercicios_resolvidos\capitulo 08\exercicio-08-13.py
##############################################################################
import random

n=random.randint(1,10)
tentativas = 0
while tentativas < 3:
    x=int(input("Escolha um número entre 1 e 10:"))
    if (x==n):
        print("Você acertou!")
        break
    else:
        print("Você errou.")
    tentativas+=1




