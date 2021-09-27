"""Somando digitos."""

numero = [75, 171, 481, 89, 516, 200, 209, 12345, 53, 27]
"""1 + 7 + 1 = 9
   9 / 171 = 0
"""
# numero = 481
#
def f(n):
    """Aqui o for faz o strip e transforma tudo em inteiro
    fazendo a divisão e chequando se igual a 0"""
    for i in n:
        i = str(i)
        x = sum(map(int, (i for i in i.strip())))
        if int(i) % x == 0:
            print("True")
            print("")
        else:
            print("Se Fudeu")
            print("")


print(f(numero))
