"""conta ocorrências
"""
import collections

lista = ('abcdeaB')
lista1 = ('abcde')
lista3 = ('abcdeee')
lista4 = ('abBBBcdeEee')
lista5 = 'aaaaaBBBBbCCCcdeee'
lista6 = ('abcdeaa')
lista7 = ('Indivisibilities')


def duplicate_count(text):

    uni = collections.Counter(text)
    show = (sorted(uni.items(), key=lambda k: -k[1]))
    return(print(show[0][1]))


duplicate_count(lista5)
