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
# Arquivo: exercicios_resolvidos\capitulo 08\exercicio-08-02.py
##############################################################################
def múltiplo(a,b):
    return a % b == 0

print("múltiplo(8,4) == True  -> obtido: %s" % múltiplo(8,4))
print("múltiplo(7,3) == False -> obtido: %s" % múltiplo(7,3))
print("múltiplo(5,5) == True  -> obtido: %s" % múltiplo(5,5))
