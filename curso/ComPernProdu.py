from itertools import count
# contador = count(start=5, step=0.1)
# for i in contador:
#     print(round(i, 2))
#     if i >=10:
#         break
from itertools import combinations
from itertools import permutations
from itertools import product


pessoas = ['Luiz', 'André', 'Eduadro', 'Jéssica', 'Camila', 'Juliana']

for pessoa in combinations(pessoas, 3):
    print(pessoa)
