from dados import produtos, pessoas, lista
from functools import reduce
# # nova_lista = filter(lambda x: x > 5, lista) usando o filter
# nova_lista = [x for x in lista if x > 5] #listcomprehesintion
# print(list(nova_lista))

# def filtra(pessoa):
#     if pessoa['idade'] < 18:
#        return True
#     return False
# novo_produtos = filter(filtra, pessoas)
# for produto in novo_produtos:
#     print(produto)
# soma_lista = reduce(lambda ac, iten: iten + ac, lista, 0)
# print(soma_lista)

# soma_idades = reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
# print(soma_idades / len(pessoas))