"""Busca Binária"""


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def buscabinary(listaordenada, num):
    """Definindo variaveis e comandos da função"""
    primeiron = 0
    ultimon = len(listaordenada) - 1

    while primeiron <= ultimon:
        half = (primeiron + ultimon) // 2
        elemento = listaordenada[half]

        if elemento < num:
            primeiron = half + 1
        elif elemento > num:
            ultimon = half - 1
        else:
            return print(f"A posição índice de {num} é: ", half)

    return print(f"O número {numx} não está na lista")


print(lista)
numx = int(input("digite um numero da lista acima: "))
buscabinary(lista, numx)
