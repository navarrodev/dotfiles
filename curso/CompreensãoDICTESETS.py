# lista = [
#     ('chave', 'valor'),
#     ('chave1', 'valor1'),
# ]
# d1 = {x: y for x, y in lista}
# print(d1, type(d1))

lista = [
    (3, 4),
    (5, 2),
]
# d1 = {x*2: y*2 for x, y in lista}
# print(d1, type(d1))
#
# d1 = {x for x in range(5)} #resultado disto é um set
# print(d1, type(d1))

d1 = {f'chave_{x}': x*2 for x in range(5)} #resultado disto é um set
print(d1, type(d1))