import sys
import time


# lista = list(range(1000))
# print(sys.getsizeof(lista)) #consultar o consumo de memória
# lista = iter(lista) #Aqui a lista agora é Iterador
# print(hasattr(lista, '__next__')) # '__next_' é um method
# print(next(lista)) #aqui para iterar literalmente

def gerador():
    for n in range(100):
        yield n
        time.sleep(0.1)


g = gerador()
for v in g:
    print(v, type(v))

# l1 = [x for x in range(1000)]  # Isto é uma lista noraml
# print(type(l1))
# l2 = (x for x in range(1000))  # Isto é um gerador, mais simples
# # do que uma função!!!
# print(type(l2))
