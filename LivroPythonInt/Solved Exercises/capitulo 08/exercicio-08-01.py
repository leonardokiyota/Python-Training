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
# Arquivo: exercicios_resolvidos\capitulo 08\exercicio-08-01.py
##############################################################################
def máximo(a,b):
    if a>b:
        return a
    else:
        return b

print("máximo(5,6) == 6 -> obtido: %d" % máximo(5,6))
print("máximo(2,1) == 2 -> obtido: %d" % máximo(2,1))
print("máximo(7,7) == 7 -> obtido: %d" % máximo(7,7))
